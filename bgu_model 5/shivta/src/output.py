import create_csv_value
import interpolate_poisson
import settings

# define folder with type 4 files, from HAZARD
data_folder = settings.folder_4_output

# define name for all finely outfile
name = settings.folder_4_output

# get poisson data from all "4" files
poisson_data = create_csv_value.create(data_folder, name)

# interpolate, and write to file
interpolate_poisson.interpolate(poisson_data, name, saveFiles=True)
