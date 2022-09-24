from csv_file import CSVFile
import pytest

def test_non_existent_file(mocker):
  # ENTRADA
  # self.path: Cualquier string me vale
  # valor de retorno de csv_file.pd.read_csv: Lanza un FileNotFoundError
  # parámetro columna: Cualquier string me vale

  # Preparar el escenario
  csv_file = CSVFile('loquesea.txt')
  mocker.patch("csv_file.pd.read_csv", side_effect=FileNotFoundError())
  # Llevar a cabo la acción y comprobar el resultado
  with pytest.raises(FileNotFoundError):
    csv_file.read_column('pepi')
  pass

def test_non_existent_column(mocker):
  # ENTRADA
  # self.path: Cualquier string me vale
  # valor de retorno de csv_file.pd.read_csv: Diccionario que NO incluya la clave "pepi"
  # parámetro columna: "pepi"

  # Preparar el escenario
  csv_file = CSVFile('loquesea.txt')
  mocker.patch("csv_file.pd.read_csv", return_value={'juani':['a', 'b', 'c']})
  # Llevar a cabo la acción
  result = csv_file.read_column('pepi')
  # Comprobar el resultado
  assert result  == []

def test_existing_column(mocker):
  # ENTRADA
  # self.path: Cualquier string me vale
  # valor de retorno de csv_file.pd.read_csv: Diccionario que incluya la clave "pepi"
  # parámetro columna: "pepi"

  # Preparar el escenario
  csv_file = CSVFile('loquesea.txt')
  mocker.patch("csv_file.pd.read_csv", return_value={'pepi':['a', 'b', 'c']})
  # Llevar a cabo la acción
  result = csv_file.read_column('pepi')
  # Comprobar el resultado
  assert result  == ['a', 'b', 'c']