import pkg_resources

# https://stackoverflow.com/questions/19086030/can-pip-or-setuptools-distribute-etc-list-the-license-used-by-each-install
# needs to run in an envinronment on which all of the packages listed in requirements.txt are installed.


def get_pkg_license(pkgname):

    pkgs = pkg_resources.require(pkgname)
    pkg = pkgs[0]

    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')

    for line in lines:
        if line.startswith('License:'):
            return line[9:]
    return '(Licence not found)'


def get_licenses(pkg_names):
    return [get_pkg_license(pkg_name) for pkg_name in pkg_names]


def pgk_names_from_requirements(pathname):
     with open(pathname, "r") as f:
        pkgs = f.read()
        pkg_names = [pkg_name.split("==")[0] for pkg_name in pkgs.split("\n") if pkg_name != ""]
     return pkg_names

def licenses_from_requirements(pathname):
    pkg_names = pgk_names_from_requirements(pathname)
    return get_licenses(pkg_names)

if __name__ == "__main__":
    print("LICENSE CHECKER:")
    print("tot num pkgs found in requirements:", len(pgk_names_from_requirements("/home/aiman/Desktop/requirements.txt")))
    licenses = licenses_from_requirements("/home/aiman/Desktop/requirements.txt")
    print("licenses found: ", len(licenses))
    print("the licenses are:", set(licenses))



