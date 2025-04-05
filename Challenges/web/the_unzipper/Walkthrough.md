# The Unzipper

This challenge was just insane and I will not elaboraty on to much detail. Here is how I solved it:

You can't inject anything into the site. You just need to upload Zip files. Everything else is just fake. The `Report the files to admin` button is just bait imo.

The main magic tricks here are: zips, linux file links and and incorrect implementation of `send_from_directory(extraction_dir, filename, as_attachment=True, download_name=filename).make_conditional(request, filename, filesize), 200`.

But lets start:

First we need to create a link to the `/proc/1/mem` file with `ln -s /proc/1/mem`. It is '1' because it's basically the only process running inside this docker container. We have to use `True` as the file name because of the incorrect impplementation of `send_from_directory`:

```python
def make_conditional(
        self,
        request_or_environ: WSGIEnvironment | Request,
        accept_ranges: bool | str = False,
        complete_length: int | None = None,
    ) -> Response:
```

Here we can see, that originally the `filename` is actually the `accept_ranges` bool. And when setting the filename to `True`, it will accept ranges.

The Zip now has to 'act' as if the symlink inside has the sice of the largest range number. Because of this code:

```python
if file['name'] == filename:
            filesize = file['length']
            break
    return send_from_directory(extraction_dir, filename, as_attachment=True, download_name=filename).make_conditional(request, filename, filesize), 200
```

We can estimate the range by just brute forcing or by running it locally and get a shell into the local version and then running `cat /proc/1/maps`. This will print out the memory regions. I'm not sure in which region the secret key will be inside, so you have to try it a few times in the worst case. For exanoke:

```
578f2000-57c0a000 rw-p 00000000 00:00 0                                  [heap]
f5c40000-f5d00000 rw-p 00000000 00:00 0
f5d00000-f5d9a000 rw-p 00000000 00:00 0
f5d9a000-f5e00000 ---p 00000000 00:00 0
```

This (maybe) needs to be converted to decimal numbers. 

Then we need to upload it. And can download the range of the mem.

```bash
curl -G -v -H "Range: bytes=4124581888-4288876544" http://localhost:1337/api/download/fe178e1605ea77d0c96b4c72308ddff21c8bb71ef66c9b41/True --output memout.bin
```

With this we can download the internal memory of the process and therefor extract the Secret key.

When you open it, you can try to look for `Adding some entropy: ` since this is the start of the key. Here is an example screenshot ![Screenshot](image.png)

With the secret key, we can generate an admin cookie and go to the `/api/flag` site and receive the flag.

The Flag: `S2G{7h15_CH4113N63_W45_700_D4mn_D1ff1CU17}`
