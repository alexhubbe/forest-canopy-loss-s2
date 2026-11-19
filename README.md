# Forest canopy loss — early warning from Sentinel-1/2 (Frankenwald, Bavaria)

> **Status:** work in progress (step 1 – setup).

## Question
1. **Early warning (main focus):** can we predict which currently intact forest pixels will lose canopy in the *next* year, using the spectral (Sentinel-2) and backscatter (Sentinel-1) trajectory of the current year?
2. **Detection (baseline):** where did the forest lose canopy between two summers?
3. **Optical vs. radar:** does Sentinel-1 add information on top of Sentinel-2?

## Study area
Frankenwald (Upper Franconia, Bavaria, Germany), a ~20 × 20 km window — see [`configs/aoi.yaml`](configs/aoi.yaml).

## Data
| Role | Source | Licence |
|---|---|---|
| Optical imagery | Sentinel-2 L2A via Microsoft Planetary Computer (STAC) | Copernicus Sentinel data |
| Radar imagery | Sentinel-1 RTC via Microsoft Planetary Computer (STAC) | Copernicus Sentinel data |
| Labels | DLR Forest Canopy Cover Loss (FCCL) Germany, 10 m, monthly | CC BY 4.0 |
| Independent validation | European Forest Disturbance Atlas (Viana-Soto & Senf) | see Zenodo record |

## Repository layout
```
src/fcl/     reusable code (STAC search, labels, indices, …)
notebooks/   analysis notebooks (run on Kaggle)
configs/     area of interest and time range
tests/       unit tests (pytest)
app/         Streamlit app (later)
```

## How to run (Kaggle)
1. New notebook → *Settings* → **Internet ON**.
2. First cell:
   ```python
   !git clone https://github.com/alexhubbe/forest-canopy-loss-s2.git
   %cd forest-canopy-loss-s2
   !pip install -q -e .
   ```
3. Open/run `notebooks/00_hello_stac.ipynb`.

## Run tests locally / in CI
```bash
pip install -e ".[dev]"
pytest
```

## Design decisions
Decisions and their rationale are logged here as the project evolves (e.g. why L2A, cloud masking, spatial cross-validation).

## Acknowledgements
Contains modified Copernicus Sentinel data. Labels: DLR Forest Canopy Cover Loss (CC BY 4.0).
