import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.config = config

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)
        """
        envs = self.config['tox']['envlist'].replace('\n', ",")
        return [env.strip() for env in envs.split(',') if env]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        py_version = set()
        for section in self.config.sections():
            for key in self.config[section]:
                if key == "basepython":
                    py_version.update([self.config[section][key]])
        return list(py_version)


if __name__ == "__main__":
    tox = ToxIniParser('cc.ini')
    print(tox.number_of_sections)
    print(tox.environments)
    print(tox.base_python_versions)
