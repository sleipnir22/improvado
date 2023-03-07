## Description

This repository contains CLI application that extracts user information from VK using VK API

## Usage
1) Install poetry:
```
    pip install poetry
```
2) Install all the dependencies
```
poetry install
```
3) Run the CLi app
```
poetry run improvado -id <user_id> -t <report_type> -o <file_name_without_extension>
```

4) Example

```
poetry run improvado -id 263626498 -t csv -o some_user_friends
```

output: some_user_friends.csv

Available report types:

| REPORT TYPE | Example          |
|-------------|------------------|
| csv         | <file_name>.csv  |                                                 |
| tsv         | <file_name>.tsv  |
| json        | <file_name>.json |

Dataschema:
```yaml
[{
   "id": 1,
   "first_name": "Name",
   "last_name": "Name",
   "country": "Russia",
   "city": "Tomsk",
   "bdate": "%d-%m-%Y",
   "sex": "male"
}]
