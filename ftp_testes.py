import ftplib
import logging
import time


host = "ftp.example.com"
username = "testuser"
password = "testpassword"


logging.basicConfig(filename="ftp_test.log", level=logging.INFO)

def test_ftp(host, username, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=username, passwd=password)
        logging.info(f"Successfully connected to {host}")

        # Measure server response time
        start_time = time.time()
        ftp.voidcmd("NOOP")
        end_time = time.time()
        response_time = end_time - start_time
        logging.info(f"Server response time: {response_time} seconds")

        # Measure download speed
        test_file = "test_file.txt"
        start_time = time.time()
        ftp.retrbinary("RETR " + test_file , open(test_file, 'wb').write)
        end_time = time.time()
        download_speed = ftp.size(test_file) / (end_time - start_time)
        logging.info(f"Download speed: {download_speed} bytes/sec")
        ftp.delete(test_file)

        # Measure upload speed
        test_file = "test_file.txt"
        start_time = time.time()
        ftp.storbinary("STOR " + test_file, open(test_file, "rb"))
        end_time = time.time()
        upload_speed = ftp.size(test_file) / (end_time - start_time)
        logging.info(f"Upload speed: {upload_speed} bytes/sec")
        ftp.delete(test_file)

        ftp.quit()
        return True
    except ftplib.all_errors as e:
        logging.error(f"Error connecting to {host}: {e}")
        return False



result = test_ftp(host, username, password)
if result:
    print("FTP test passed")
else:
    print("FTP test failed")
