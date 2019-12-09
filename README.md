
# Account Links Generator

This is a python tool to generate a set of markdown formatted tables from an AWS config.yaml file to enable users to easily find an assume an AWS IAM role for each specific environment contained in the .yaml file.

## Usage

The program accepts 4 arguments: 
 - **--config** - the path to the desired .yaml config file
 - **--output** - the desired path of the markdown-formatted output 
 - **--intro** - the path to any text to be displayed *before* the markdown tables (optional)
 - **--outro** - the path to any text to be displayed *after* the markdown tables (optional)
### License

This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
