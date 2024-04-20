## Available endpoints per service

### Infra-service

- [GET] /devices \
  Get all registered devices. \
  Returns:

  - nested dictionary with device_id as main key

  ```json
  {
    "1": {
      "id": 1,
      "model": 1,
      "owner": 1,
      "name": "Strawberry",
      "comment": null
    },
    "2": {
      "id": 2,
      "model": 1,
      "owner": 2,
      "name": "Blueberry",
      "comment": null
    }
  }
  ```

- [GET] /devices/owners/\<owner_id> \
   Get all registered devices belonging to particular user. \
   Params:

  - owner_id (int): id of the owner

  Returns:

  - nested dictionary with device_id as main key with devices belonging to chosen owner

  ```json
  {
    "1": {
      "id": 1,
      "model": 1,
      "owner": 1,
      "name": "Strawberry",
      "comment": null
    },
    "2": {
      "id": 2,
      "model": 1,
      "owner": 1,
      "name": "Blueberry",
      "comment": null
    }
  }
  ```

- [POST] /devices \
  Register new device. \
  Params:

  - owner (int): id of the owner
  - model (int/str): id or name of the model

  Request:

  ```json
  {
    "owner": "1",
    "model": "Sensor-M100"
  }
  ```

  Returns:

  - 200, success: true

- [GET] /models \
  Get all models.

  Returns:

  - TODO

- [POST] /models \
   Add new model. \
  Params:

  - category (int): id of the category
  - manufacturer (int): id of the manufacturer
  - name (str): name of the model
  - energy_cons (float): energy consumption of the model

  Request:

  ```json
  {
    "category": "1",
    "manufacturer": "1",
    "name": "Termometer-100S",
    "energy_cons": "1.5"
  }
  ```

  Returns:

  - 200, success: true

- [GET] /categories \
  Get all categories. \

  Returns:

  - TODO

- [POST] /categories \
   Add new category. \
  Params:

  - name (str): name of the category

  ```json
  {
    "name": "termometers"
  }
  ```

  Returns:

  - 200, success: true

- [GET] /getConsumption/models/\<model_name\> \
   Get calculated energy consumption for all devices from provided model. \
  Params:

  - model_name (str): name of the model

  Returns:

  ```json
  {
    "model_id": "1",
    "model_name": "Termometer-100S",
    "total_energy_consumption": "17.7"
  }
  ```

### Geo-service

- [GET] /positions/\<device_id\> \
  Get position of given device. \
  Params:

  - device_id (int): id of the device

  Returns:

  ```json
  {
    "position_x": 1.7,
    "position_y": 2.0
  }
  ```

- [POST] /positions \
  Add new device's position. \
  Params:

  - device_id (int): id of the existing device
  - pos_x (float): position x of the device
  - pos_y (float): position y of the device

  Returns:

  - 200, success: true

- [GET] /positions/recommend/\<owner_id> \
  Get recommended position for user's device. \
  Calculated as: pos_x - average of position_x from all user's devices, pos_y - average of position_y from all user's devices. Simulates some more complex computations.

  Params:

  - owner_id (int): id of the owner

  Returns:

  ```json
  {
    "position_x": 1.7,
    "position_y": 2.0
  }
  ```

### Stats-service

- [GET] /metrics \
  Get all available metrics.

  Returns:

  - nested dictionary with metric_id as main key

  ```json
  {
    "1": {
      "id": 1,
      "name": "temperature [C]"
    },
    "2": {
      "id": 2,
      "name": "temperature [K]"
    }
  }
  ```

- [GET] /metrics/devices/\<device_id\> \
  Get all available metrics for chosen device. \
  Params:

  - device_id (int): id of the device

  Returns:

  - nested dictionary with metric_id as main key

  ```json
  {
    "1": {
      "id": 1,
      "name": "temperature [C]"
    },
    "2": {
      "id": 2,
      "name": "temperature [K]"
    }
  }
  ```

- [GET] /values/devices/\<device_id\>/\<metric_id\>/\<max_number\> \
  Get max_number of most recent observed values for chosen metric and device.\
  Params:

  - device_id (int): id of the device
  - metric_id (int): id of the metric
  - max_number (int): max number of inquired observed values

  Returns:

  - list of the observed values with timestamps

  ```json
  {
    "1": {
      "device_id": 1,
      "metric_id": 1
    },
    "2": {
      "id": 2,
      "name": "temperature [K]"
    }
  }
  ```

- [GET] /values/owner/\<owner_id\>/metrics/\<metric_id\> \
  Get latest observed value for specified metric from all owner's devices.\
  Params:

  - owner_id (int): id of the owner
  - metric_id (int): id of the metric

  Returns:

  - a list of latest observed values of particular metric, for all devices with that metric belonging to provided user id.

  ```json
  [
    {
      "id": 1,
      "metric": 1,
      "timestamp": "2024-04-17 21:57:09",
      "value": 15.5
    },
    {
      "id": 2,
      "metric": 1,
      "timestamp": "2024-04-17 22:57:09",
      "value": 17.5
    }
  ]
  ```

- [GET] /stats/devices/\<device_id\>/\<metric_id\>/\<count\> \
  Get statistics about most recent <count> number of device_id for metric_id.\
  Params:

  - device_id (int): id of the device
  - metric_id (int): id of the metric
  - count (int): number of required latest observed values

  Returns:

  - statistics for given device: min, max and avg

  ```json
  {
    "avg": 10.2,
    "max": 20,
    "min": 8.1
  }
  ```
