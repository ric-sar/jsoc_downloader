# JSOC Downloader
Script to download data from Joint Science Operations Center (JSOC)

# Requirements
- [sunpy](https://docs.sunpy.org/en/stable/tutorial/installation.html) 

# How to
There are arguments to use to start downloading data:
- Start date
- End date
- Series
- E-mail

## Example
```
python sunpy_downloader.py --start 2014-01-01T00:00:00 --end 2014-01-01T00:01:00 --series hmi.v_45s --mail name@domain.com
```

# FAQ
Please use the [**sunpy documentation**](https://docs.sunpy.org/en/stable/tutorial/acquiring_data/index.html) to improve the script
