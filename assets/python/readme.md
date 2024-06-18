### How to update face names
1. Update the names in `.collections/_faces/` to be the correct ones - it's most important to change the `short_name` attribute in the `.md` files, but the filenames should be updated as well.
2. Change `utils.py::SHOULD_OVERWRITE_CURRENT_FILES` to `return True`
3. Run `python generate_cases.py`.  You probably should delete previous files first.
4. Follow the "How to update algs from OBL spreadsheet" section for updating other affected sections.

### How to update algs from OBL spreadsheet
1. Download from Google Sheets as TSV's.
2. Change `utils.py::SHOULD_OVERWRITE_CURRENT_FILES` to `return True`.
3. Run `python fix_csv_titles.py` first - this fixes the CSV titles to have unique headers
	a. TODO: just fix these in the spreadsheet itself
4. Run `python import_csvs.py` - this generates the right information in the case `.md` files
5. If any algs have different angles/names, run `python download_case_images.py`.  You probably should delete previous files first.
