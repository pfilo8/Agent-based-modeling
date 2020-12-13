# Convay's Game of Life

In this assignment list we've implemented Convay's Game of Life.
We've made it in very generic way. Especially, it's possible to:
* Change boundary condition (periodic or not)
* Alive conditions, i.e. for which number of alive neighbours given cell stays alive
* Dead conditions, i.e. for which number of alive neighbours given cell it's reproduced and become alive
* To automatically detect which fields in given by user grid are dead and which are alive

### Grid configuration
It should be a text file which contains two different chars which corresponds to dead and alive cells.

### Configuration
To run model you need to provide configuration. Only required field is `grid_filename`.
Default values for rest of the fields are provided below.
```json
{
  "grid_filename": "",
  "torus": true,
  "alive_condition": [2, 3],
  "dead_condition": [3],
  "alive_char": null,
  "dead_char": null,
  "max_iter": 150
}
```
Fields `alive_char` and `dead_char` are optional and if not provided the config parser tries to find out these values.

Examples are provided in `configs` directory.
You can run script by `run_example.sh` bash script.

### Example
1. Simple example - automatic parsing of default values
2. Non periodic boundaries, interesting still forms and simple periodic forms
3. Different alive / dead conditions for forms which were still in original game. In particular alive cell stays alive for [2, 3, 4] alive neighbours and dead cell is reproduced for 2 neighbours.
