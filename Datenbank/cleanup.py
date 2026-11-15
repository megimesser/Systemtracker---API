# Retention Policy: löscht Daten älter als RETENTION_TAGE
import sys
import time

import psycopg2
from psycopg2 import sql

from config import DATABASE_DB, DATABASE_PW, DATABASE_USER

RETENTION_TAGE = 7
MAX_VERSUCHE = 5
TABELLEN = ["temperaturinformation","cpuinformation","dockerinformation","prozessinformation","discinformation","hostinginformation","prozessinformation","raminformation","sysinformation"]


def verbinden():
    for versuch in range(1, MAX_VERSUCHE + 1):
        try:
            return psycopg2.connect(
                host="localhost", port=5433,
                dbname=DATABASE_DB, user=DATABASE_USER, password=DATABASE_PW,
            )
        except psycopg2.OperationalError as error:
            print(f"Verbindung fehlgeschlagen (Versuch {versuch}/{MAX_VERSUCHE}): {error}")
            time.sleep(2)
    return None


def retention_policy(conn, tage: int) -> None:
    with conn.cursor() as cursor:
        for tabelle in TABELLEN:
            cursor.execute(
                sql.SQL("DELETE FROM {} WHERE erfasst_am < now() - make_interval(days => %s)")
                .format(sql.Identifier(tabelle)),
                (tage,),
            )
            print(f"{tabelle}: {cursor.rowcount} Zeilen gelöscht")
    conn.commit()


def main() -> int:
    conn = verbinden()
    if conn is None:
        print("Abbruch: keine Datenbankverbindung")
        return 1
    try:
        retention_policy(conn, RETENTION_TAGE)
        return 0
    except psycopg2.Error as error:
        conn.rollback()
        print(f"Fehler beim Löschen: {error}")
        return 1
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())