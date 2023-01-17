# **PydTfinder**
> ::A tool to find the phase eq temperature at a given pressure with a given ΔT value::

<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

PydTfinder is a cutting-edge and user-friendly tool that makes it easy to pinpoint the precise temperature and pressure points where phase transitions occur in your system. If you're working with Hydrate-Liquid-Vapor equilibrium systems, PydTfinder is the perfect tool to help you find the exact equilibrium point of interest you need. By utilizing a temperature difference input and a highly accurate polynomial regression algorithm, PydTfinder is able to identify the precise points of phase transition with pinpoint accuracy. This powerful tool also offers a wide range of customization options, including `manual input`, `csv file input`, `output type`, `degree of regression`, `number of points` displayed in the plot, and `directory location` of the csv file, allowing you to tailor the tool to your specific needs. For researchers, engineers, and scientists working in the field of thermodynamics, phase equilibrium, and phase transition, PydTfinder is an essential tool that will save you time and increase your productivity.

## **Features**
- Plot the phase equilibrium data and the regression line
- Also plot the parallel line according to the temperature difference ($\Delta T$ value)
- Input options include `manual` input or input from a `csv` file
- Allows for adjusting the degree of the regression (the higher the degree, the more accurate the regression) and the number of points displayed in the plot
- Output options include `png`, `pdf`, `svg`, and `eps` file types

## **Dependencies**
- `pandas`
- `argparse`
- `pyfiglet`
- `tabulate`
- `matplotlib`
- `numpy`
- `sklearn`

## **Installation**
```
$ pip install pydtfinder
```
or
```
$ pip3 install pydtfinder
```

## **Uninstallation**
```
$ pip uninstall pydtfinder
```
or
```
$ pip3 uninstall pydtfinder
```

## **Usage**
The tool can be run using the command line 

```
$ pydtfinder
```

### **Optional arguments**
| Argument | Short form | Default | Description |
| --- | --- | --- | --- |
| `--input_type` | `-it` | manual | The type of P, T input. The options are: `manual`, `csv`|
| `--delta_t` | `-dt` | 5 | The temperature difference between the two curves in K |
| `--degree` | `-g` | 5 | The degree of the regression; the higher the degree, the more accurate the regression |
| `--num_point` | `-n` | 10 | The number of points that will be expressed in the plot |
| `--output` | `-o` | png | The file type of the output file. The options are: png, pdf, svg, and eps |
| `--directory` | `-d` | "./" | The directory location of the csv file |
| `--legend` | `-l` | "Your Phase EQ input" | The legend title of your Phase EQ input data |
| `--version` | `-v` | | Show the version of the tool |

## **Contact**
If you have any questions or suggestions, please visit the GitHub repository at https://github.com/wjgoarxiv/pydtfinder for more information.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **Pull requests**
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
