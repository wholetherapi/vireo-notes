# Vireo-Notes

Experiment code for **Vireo-Notes**, a study of rolling schema evolution in
append-only event stores.

## Contents

- `src/vireo/schema.py` - schema versioning and compatibility checks.
- `experiments/evolution_notes.md` - the evolution scenarios used in the study.

## Usage

```bash
pip install -r requirements.txt
python -m vireo.schema --scenario experiments/evolution_notes.md
```

## License

MIT.
