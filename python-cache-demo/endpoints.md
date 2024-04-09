## Available endpoints per service

### Infra-service

- [GET] /devices \
  Get all registered devices. \
  Returns:
  - TODO
- [GET] /devices/\<owner_id> \
   Get all registered devices belonging to particular user. \
   Params:

  - owner_id (int): id of the owner

  Returns:

  - TODO

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

#### TODO

- [PUT] /devices/\<device_id\> \
   Update information about registered device of given id.
  Params:
  - device_id (int): id of the device
- [PUT] /models/\<model_id\> \
   Update information about given model.
  Params:
  - model_id (int): id of the model
- [PUT] /categories/\<category_id\> \
   Update information about given category.
  Params:
  - category_id (int): id of the category

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

#### TODO:

- [GET] /positions/owners/\<owner_id\> \
  Get positions of all devices belonging to particular owner.
  Params:
  - owner_id (int): id of the owner
- [PUT] /positions/\<device_id\> \
   Update position of given device.
  Params:
  - device_id (int): id of the device

### Stats-service

- [GET] /metrics \
  Get all available metrics.

#### TODO:

- [GET] /values/\<device_id\> \
  Get most recent observed value for chosen device.

  Params:

  - device_id (int): id of the existing device

- [GET] /stats/\<device_id\>/\<time_period\> \
  Get statistics about observed values for chosen device since specified time period. Values taken from present to \<time_period\> in the past.

  Params:

  - device_id (int): id of the existing device
  - time_period (str): time period for the statistics in the form \<number\>\_\<units\>. Supported units: s (seconds), m (minutes), h (hours), d (days)

Endpoints suggestions to be added...
