# Simulator

`ispyb.simulate` creates a new DataCollection row in the ISPyB database from a simple yaml definition. It creates a data collection, related sample information, and associated shipping entities. It then copies some raw data and associated snapshots (and thumbnails).

Simulate a data collection:

```bash
ispyb.simulate <beamline> <experiment>
ispyb.simulate bm23 energy_scan1
```

The simulator will create hierarchically a component (`Protein`), related `BLSample` (with intermediate `Crystal`), and potentially a `SubSample`, contained within a `Container`, `Dewar`, and `Shipment` belonging to the specified `Proposal` if they do not already exist with the defined name. Then the simulator creates a `DataCollection` and `DataCollectionGroup`, linked to the relevant `BLSample` and `BLSession`. If grid info information is specified it will also create an entry in `GridInfo`

## Configuration

The configuration file location is defined via the `SIMULATE_CONFIG` environment variable. An example configuration is available in `examples/simulation.yml`. The structure and requirements of this file are documented in the example.

Each entry in `experiments` represents a different data collection. The `experimentType` column relates to a `DataCollectionGroup.experimentType` entry so must match one of the available types in the database. See [experimentType](https://github.com/ispyb/ispyb-database/blob/main/schema/1_tables.sql#L1518)s for a full list.

## Available columns per table

The ISPyB tables are large, and as such only a subset of the columns are exposed by this simulator, the most pertinent in order to create usable data collections and associated entries. These are as listed below for each table.

### Component (Protein)

- acronym
- name
- sequence
- density
- molecularMass
- description

### BLSample

- name

### BLSubSample

- x
- y
- x2
- y2
- type

### DataCollection

- imageContainerSubPath
- numberOfImages
- wavelength
- exposureTime
- xtalSnapshotFullPath1-4

### GridInfo

- steps_x
- steps_y
- snapshot_offsetXPixel
- snapshot_offsetYPixel
- dx_mm
- dy_mm
- pixelsPerMicronX
- pixelsPerMicronY

## Plugins

The simulator can trigger events before and after the data is copied using the `ispyb.simulator.before_datacollection` and `ispyb.simulator.after_datacollection` entry points. These are passed just the new `DataCollection.dataCollectionId`.
