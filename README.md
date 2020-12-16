
# Account Links Generator

This is a python tool to generate a set of markdown formatted tables from an AWS config.yaml file to enable users to easily find and assume an AWS IAM role for each specific environment contained in the .yaml file.

## Usage

The program accepts 4 arguments:
 - **--config** - the path to the desired .yaml config file
 - **--output** - the desired path of the markdown-formatted output
 - **--intro** - the path to any text to be displayed *before* the markdown tables (optional)
 - **--outro** - the path to any text to be displayed *after* the markdown tables (optional)

## Docker
Build an image locally:
```shell
docker build -t hmrc/account-links-generator:1.0.0 .
```

Run the image, assuming a local `output` directory and `config/config.yaml` file exist on the host:
```shell
docker run --rm \
       -v $(pwd)/config.yaml:/config.yaml \
       -v $(pwd)/output:/output \
       hmrc/account-links-generator:1.0.0 \
       python accountlinks_generator/__main__.py \
       --config "/config.yaml" \
       --output "/output/output.md"
```

## License
This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
