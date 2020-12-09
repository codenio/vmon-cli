# vmon-cli

vmon-cli - CLI Viewer for Ibsen 512 USB interrogator


## Installation

```bash
# clone the repository
$ git clone git@github.com:codenio/vmon-cli.git

# move into tmon-cli folder
$ cd vmon-cli

# install requirements
$ pip install -r requirments.txt

# intall tmon
$ pip install .

# check installation
$  vmon
Usage: vmon [OPTIONS] COMMAND [ARGS]...

  vmon - I-Mon Spectrum Viewer and Exporter

Options:
  --help  Show this message and exit.

Commands:
  plot    Plot the I-Mon data into graphs

```

### Usage

- vmon commands
    ```bash 
    $ vmon
	Usage: vmon [OPTIONS] COMMAND [ARGS]...

	  vmon - I-Mon Spectrum Viewer and Exporter

	Options:
	  --help  Show this message and exit.

	Commands:
	  plot    Plot the I-Mon data into graphs
    ```
- plot sub command
    ```bash
    $ vmon plot --help
	Usage: vmon plot [OPTIONS] FILES...

	  Plot the I-Mon data into graphs

	Options:
	  -p, --path TEXT   path form which csv files are to be imported, default = .
	  -t, --title TEXT  set custom title for the plot, default = .
	  -n, --normalise   normalise the data before ploting
	  -pk, --peaks      show peaks in the plot
	  --help            Show this message and exit.
    ```

### Examples

- Plot Command
    ```bash
    $ vmon plot -p ./data/ 1530_1.1.csv 1530_2.2.csv
    ```

<p align="center">
  <img src="docs/images/demo.png">
</p>

- Plot Command with customised title, peaks and zoomed
	```bash
	$ vmon plot -p ./data/ 1530_1.1.csv 1530_2.2.csv -pk -t "FBG Spectrums"
	```

<p align="center">
  <img src="docs/images/demo-customised.png">
</p>
