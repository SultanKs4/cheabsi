from absen import absen

if __name__ == "__main__":
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    absen = absen(username, password)
    absen.login()
    absen.presensi()
    absen.create_log()
