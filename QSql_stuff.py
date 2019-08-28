from PyQt5.QtSql import *


def save_ip_mac_to_db(self, ip, mac):
    print("Attempting to save to db")
    self.query.prepare("INSERT INTO live_hosts (ip_address, mac_address)"
                       "VALUES (?, ?)")
    self.query.addBindValue(ip)
    self.query.addBindValue(mac)
    if not self.query.exec_():
        print(self.query.lastError().text())
        return False
    while self.query.next():
        print(self.query.value(0))


def update_db(self):
    print("Attempting to update db:")

    self.query = QSqlQuery()

    self.query.prepare("SELECT EXISTS(SELECT 1 FROM live_hosts WHERE ip_address='192.168.1.154')")
    if not self.query.exec_():
        print("Ooops")
        print(self.query.lastError().text())
        return False
    while self.query.next():
        print(self.query.value(0))
    print(self.query.lastError().text())