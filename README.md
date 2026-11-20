# Forest canopy loss — early warning from Sentinel-1/2 (Frankenwald, Bavaria)

> **Status:** work in progress (step 1 – setup).

## Question
1. **Early warning (main focus):** can we predict which currently intact forest pixels will lose canopy in the *next* year, using the spectral (Sentinel-2) and backscatter (Sentinel-1) trajectory of the current year?
2. **Detection (baseline):** where did the forest lose canopy between two summers?
3. **Optical vs. radar:** does Sentinel-1 add information on top of Sentinel-2?

## Study area
Frankenwald (Upper Franconia, Bavaria, Germany), a ~20 × 20 km window — see [`configs/aoi.yaml`](configs/aoi.yaml).

### Why the Frankenwald?
- **A documented hotspot of canopy loss.** Using stereo aerial imagery, the Bavarian State Institute of Forestry (LWF) estimated that 71.73 km² (± 0.78 km²) of clear-cut area appeared in the Frankenwald between May 2017 and October 2022 — 15% of the total forest area of growth region 8.1 Frankenwald. The same article, reviewing the 2022 bark-beetle season, reports that the highest densities and trap counts of the spruce bark beetle (*Ips typographus*, "Buchdrucker") were recorded in the Frankenwald (citing Triebenbacher et al. 2023), and that the large clear-cuts are a result of the mass bark-beetle infestation [1].
- **A clear temporal dynamic.** Trap counts of spruce bark beetles (mainly *Ips typographus* and *Pityogenes chalcographus*) in the Frankenwald rose sharply from 2018 and peaked, so far, in 2020 [2]. The study period (2017–2024) therefore covers the years before, during and after the outbreak — the setting needed to test whether stress is visible *before* canopy loss.
- **Label and validation data are available.** The DLR FCCL product covers all of Germany at 10 m with monthly loss dates, and the European Forest Disturbance Atlas provides an independent reference (see *Data*).

The exact ~20 × 20 km window is provisional; it will be fixed in step 2 so that it contains both abundant canopy loss and abundant intact forest.

**References**
1. Straub, C., Wallner, A., Reinosch, E. & Seitz, R. (2023). *Mit Luftbildern Borkenkäferschäden erfassen.* LWF aktuell 3/2023 (no. 140). Bayerische Landesanstalt für Wald und Forstwirtschaft. [PDF](https://lfl.bayern.de/mam/cms04/informationstechnologie/dateien/mit_luftbildern_borkenk%C3%A4fersch%C3%A4den_erfassen_-_lwf_aktuell_140.pdf)
2. Hahn, A., Lemme, H. & Landgrebe, J. (2021). *Kann Silofolie Fichtenborkenkäfern den Garaus machen?* waldwissen.net (LWF, Abt. Waldschutz), 06.12.2021; based on Schißlbauer, J., Lemme, H. & Hahn, A. (2021). [Link](https://www.waldwissen.net/de/waldwirtschaft/holz-und-markt/lagern-und-konservieren/kann-silofolie-fichtenborkenkaefern-den-garaus-machen)

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
