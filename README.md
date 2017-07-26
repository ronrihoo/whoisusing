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


`-a` : Return the actual filename associated with found processes

```
$ whoisusing cups -a
root	cupsd cups-browsed 
lp	dbus
```

The actual filenames retrieved for each user are separated from each other by a space.


`-s` : Returns only the results that have matching filenames

Notice the actual name above for user `lp` is too different from the searched name `cups`. In order to prevent this, the strict option flag, `-s`, will ensure that the associated filenames are a close match to the searched named.

```
whoisusing cups -s
root
```
Additionally, one may combine options for more detailed results, like so:

```
$ whoisusing cups -sa
root	cupsd 
```


`-p` : Return users with their associated PIDs

```
$ whoisusing mysql -p
mysql   1412
```
Similar to `ps aux | grep mysql | awk '{ print $1,  $2 }'` with the difference being that all of the associated PIDs of each unique user are listed on the same line, like so:

```
$ whoisusing mysql -p
mysql   1412 1413
```

-where the latter would display:

```
$ ps aux | grep mysql | awk '{ print $1,  $2 }'
mysql 1412
mysql 1413
```

`-d` : Return the directories associated with the user who's using the specified process

```
$ whoisusing cups -d
root	/usr/sbin/cupsd /usr/sbin/cups-browsed 
lp	/usr/lib/cups/notifier/dbus 
```

This can be combined with other options.

```
$ whoisusing cups -apd
root	cupsd 3703 cups-browsed 3704 
	/usr/sbin/cupsd /usr/sbin/cups-browsed 
lp	dbus 3712 
	/usr/lib/cups/notifier/dbus 
```


`-l` : Return the lines that were used to determine who the users are

```
$ whoisusing mysql -l
mysql     1412  0  1.5 1253291 156937 ?      Ssl  00:20   0:01 /usr/sbin/mysqld

mysql
```
The line returned is exactly similar to the output of `ps aux | grep mysql`. In case of multiple results, first all of the lines will be printed in the same respective order as the user names which follow.


## Removal

Using terminal, run the following command:

```
$ sudo /usr/local/bin/whoisusing-1.0/remove.sh
```

If `whoisusing` was placed somewhere else, then one may use the `--whereami` option to find where it is.

```
$ whoisusing --whereami
```

This is the same as the following command:

```
$ whereis whoisusing
```

A directory should be returned, like so:

```
whoisusing: /usr/local/bin/whoisusing
```

If that fails, then an additional method of finding `whoisusing` has been provided with the `--findme` flag.

```
$ whoisusing --findme
```

This is the same as invoking the command:

```
$ find / -name "whoisusing" 2>/dev/null
```

-from which one would normally expect to receive the following result:

```
/usr/local/bin/whoisusing
/usr/local/bin/whoisusing-1.0/whoisusing
```

From the found directory, run the `remove.sh` script using `sudo`.


## Remarks

In general, `whoisusing` requires more work, as there is more to be desired. However, it does its job as a quick CLI tool.

## Contributing

All pull requests are welcome. 

