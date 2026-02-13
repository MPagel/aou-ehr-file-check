import inspect
import os
import foundry_stuff as fdry

base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
resource_path = os.path.join(base_path, 'resources')
html_boilerplate = os.path.join(resource_path, 'html_boilerplate.txt')
test_path = os.path.join(base_path, 'tests')
test_resource_path = os.path.join(test_path, 'resources')
example_path = os.path.join(test_resource_path, 'examples_erroneous')
cdm_metadata_path = os.path.join(resource_path, 'omop')

# Configuration
files_to_check = fdry.unzip_imported_zip('input_resource')
csv_dir = fdry.extract_dl_location(files_to_check) # 'path/to/csv_files'  # location of files to validate, evaluate
