# Readme

- [Dependency](#Dependency)
- [Install](#install)
- [Usage](#usage)
	- [Generator](#generator)
- [Badge](#badge)
- [Example Readmes](#example-readmes)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Dependency
```
sudo apt-get install libmysqlclient-dev -y
# or centos7
sudo yum install mysql-devel -y
```

## Install
```
mkdir -p  /var/avatr/static
mkdir /var/log/avator

pip install -r requirements.txt

cp config/supvisor_phthisis.conf /etc/supervisor/conf.d/
supervisorctl reload

```
