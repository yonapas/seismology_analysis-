import create_csv_value
import interpulate_poisson
import settings

# define folder with type 4 files, from HAZARD
data_folder = settings.folder_4_output

# define name for all finely outfile
name = settings.parameters

# get poisson data from all "4" files
poisson_data = create_csv_value.create(data_folder, name)

# interpolate, and write to file
interpulate_poisson.interpulate(poisson_data, name, saveFiles=True)
