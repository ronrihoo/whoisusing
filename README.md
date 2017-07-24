# whoisusing
A Python script for Linux which displays the local users who are using a specified application or service.

## Setup
Clone this repository or download the zip and extract contents to a local directory.

Using terminal, navigate to the `whoisusing` directory and run the following commands:

```
$ chmod +x ./setup.sh
$ sudo ./setup.sh
```
This will create a directory in `/usr/local/bin/` named `whoisusing-1.0` and it will also add a symlink of `/usr/local/bin/whoisusing-1.0/whoisusing` to `/usr/local/bin/`.

## Usage

`whoisusing <name> <option>` 

Example:
```
$ whoisusing mysql
mysql
```
The output is the name of the user.

Options:

`-p` : Return users with their associated PIDs

```
$ whoisusing mysql -p
mysql   1412
```
Similar to `ps aux | awk '{ print $1,  $2 }' | grep mysql` with the difference being that all of the associated PIDs of each unique user are listed on the same line, like so:

```
$ whoisusing mysql -p
mysql   1412 1413
```

-where the latter would display:

```
$ sudo ps aux | awk '{ print $1,  $2 }' | grep mysql
mysql   1412
mysql   1413
```

`-l` : Return the lines that were used to determine who the users are

```
$ whoisusing mysql -l
mysql     1412  0  1.5 1253291 156937 ?      Ssl  00:20   0:01 /usr/sbin/mysqld

mysql
```
The line returned is the output of `ps aux | grep mysql`. In case of multiple results, first all of the lines will be printed in the same respective order as the user names which follow.

## Removal

Using terminal, run the following command:

```
$ sudo /usr/local/bin/whoisusing-1.0/remove.sh
```

If `whoisusing` was placed somewhere else, then find out where it is:

```
$ whereis whoisusing
```

A directory should be returned, like so:

```
whoisusing: /usr/local/bin/whoisusing
```

If that fails, then one may try other means of searching for the filename, such as:

```
$ sudo find / -name "whoisusing" 2>/dev/null
```

-from which one would normally expect to receive the following result:

```
/usr/local/bin/whoisusing
/usr/local/bin/whoisusing-1.0/whoisusing
```

Find and run the `remove.sh` script.

## Remarks

In general, `whoisusing` requires a lot of work; although, it does its job as a quick CLI tool. There is more to be desired, but it's not bad for a half hour's worth of coding.

## Contributing

All pull requests are welcome. 

