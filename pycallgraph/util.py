class Util(object):

    @staticmethod
    def human_readable_bibyte(num):
        num = float(num)
        for x in ['B', 'KiB', 'MiB', 'GiB']:
            if num < 1024 and num > -1024:
                return '{0:3.1f}{1}'.format(num, x)
            num /= 1024
        return '{0:3.1f}{1}'.format(num, 'TiB')
