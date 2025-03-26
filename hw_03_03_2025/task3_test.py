import os
import pytest
from task3 import FileManager  

@pytest.fixture
def file_manager():
    return FileManager()

def test_write_read_text_file(file_manager):
    filename = 'test.txt'
    content = 'Hello, World!'
    file_manager.write_file(filename, content)
    assert file_manager.read_file(filename) == content
    os.remove(filename)

def test_write_read_json_file(file_manager):
    filename = 'test.json'
    data = {'name': 'Alice', 'age': 30}
    file_manager.write_file(filename, data)
    assert file_manager.read_file(filename) == data
    os.remove(filename)

def test_write_read_csv_file(file_manager):
    filename = 'test.csv'
    data = [['name', 'age'], ['Alice', 30], ['Bob', 25]]
    file_manager.write_file(filename, data)
    assert file_manager.read_file(filename) == [['name', 'age'], ['Alice', '30'], ['Bob', '25']]
    os.remove(filename)

def test_read_nonexistent_file(file_manager):
    with pytest.raises(FileNotFoundError, match="file nonexistent.txt не найден."):
        file_manager.read_file('nonexistent.txt')

def test_delete_file(file_manager):
    filename = 'test_delete.txt'
    file_manager.write_file(filename, 'этот файл будет удален')
    file_manager.delete_file(filename)
    with pytest.raises(FileNotFoundError, match="test_delete.txt найден."):
        file_manager.read_file(filename)

def test_delete_nonexistent_file(file_manager):
    with pytest.raises(FileNotFoundError, match="nonexistent.txt найден."):
        file_manager.delete_file('nonexistent.txt')

if __name__ == "__main__":
    pytest.main()