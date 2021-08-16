# Command Injection Tester

The `command-injection-tester` script allows for straightforward testing of email servers for the STARTTLS command injection vulnerability in SMTP, POP3, and IMAP. 

## Usage

The command

`python3 command-injection-tester --imap --pop3 --smtp <hostname>`

tests `<hostname>` for the command injection in IMAP, POP3, and SMTP.

## Parameters

* `--help` (`-h`): Print help message.
* `--imap`: Use the IMAP protocol
* `--pop3`: Use the POP3 protocol
* `--smtp`: Use the SMTP protocol
* `--imap-port` (`-i`): IMAP port to check (default: 143)
* `--pop3-port` (`-p`): POP3 port to check (default: 110)
* `--smtp-port` (`-s`): SMTP port to check (default: 587)
* `--quiet` (`-q`): Be less verbose
* `--timeout` (`-t`): Timeout in seconds to use for network sockets. Increase in case of problems (default: 2)
* `--logdir` (`-l`): Path to log directory (default: `./logs`)

## Example:

The Command Injection Tester can best be tested using the [Fake Mail Server](https://github.com/Email-Analysis-Toolkit/fake-mail-server):

1. Start the `Fake Mail Server`:

```sh
$ sudo ./fake_mail_server setup
```

2. Run this script against the server:

```sh
$ python3 command-injection-tester --imap --pop3 --smtp localhost
```

3. Since the Fake Mail Server is intentionally vulnerable against the command injection, you should see `Command injection here!` after every protocol test.

Testing live servers should be just as easy. If connections keep timing out/the sanity test keeps failing, try increasing the timeout using the `--timeout` parameter.

## Background

This tool was published as part of our research on security vulnerabilities in STARTTLS:

* https://nostarttls.secvuln.info/
