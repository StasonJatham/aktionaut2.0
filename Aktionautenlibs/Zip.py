import zipfile

class Zip:
    """
    USAGE:
        from Zip import Zip
        Zip("DB/AKTIONAUT.db","DB_BACKUP/db_backup").zip()
    """

    def __init__(self, data_file_name, backup_file_name):
        self.data_file_name   = data_file_name
        self.backup_file_name = backup_file_name

    def zip(self):
        with zipfile.ZipFile('{}.zip'.format(self.backup_file_name), 'w') as myzip:
            myzip.write('{}'.format(self.data_file_name))



