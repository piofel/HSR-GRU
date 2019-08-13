import pandas as pd

from hsr.config import RESOURCES_DIR, HS_DATABASE_DIR
from hsr.file_io import file_io_json
from hsr.file_io.file_manager import safely_remove_file
from hsr.preprocessing.config import HS_DB_FILENAME_EXTENSION
from hsr.preprocessing.config import ROMAN_TEXT_LABEL, ENGLISH_TEXT_LABEL

COLUMN_NAMES = ['COUNTRY_NAME', 'HS_DB_NAME', 'HS_DB_CHARACTERS_TYPE', 'HS_DB_RECORDS_STRUCTURE', 'REMARKS']
COUNTRY_NAME_COL_INDEX = 0
HS_DB_NAME_COL_INDEX = 1
HS_DB_CHARACTERS_TYPE_COL_INDEX = 2
HS_DB_RECORDS_STRUCTURE_COL_INDEX = 3
REMARKS_COL_INDEX = 4
EXCEL_FILENAME = RESOURCES_DIR + 'countries_metadata.xlsx'
JSON_FILENAME = RESOURCES_DIR + 'countries_metadata.json'


def get_metadata():
    records = append_countries([])
    data = finish_data_initialization(records)
    safely_remove_file(EXCEL_FILENAME)
    safely_remove_file(JSON_FILENAME)
    return data


def get_database_filename(countries_metadata, country_index):
    return HS_DATABASE_DIR + get_hs_db_name(countries_metadata, country_index) + HS_DB_FILENAME_EXTENSION


def countries_names(countries_metadata):
    return [get_country_name(countries_metadata, i) for i in range(get_number_of_countries(countries_metadata))]


def save_as_excel(countries_metadata):
    countries_metadata.to_excel(EXCEL_FILENAME)


def save_as_json(countries_metadata):
    file_io_json.save(countries_metadata, JSON_FILENAME)


def get_number_of_countries(countries_metdata):
    (n, _) = countries_metdata.shape
    return n


def get_country_name(countries_metdata, country_index):
    return countries_metdata.iat[country_index, COUNTRY_NAME_COL_INDEX]


def get_hs_db_name(countries_metdata, country_index):
    return countries_metdata.iat[country_index, HS_DB_NAME_COL_INDEX]


def get_hs_db_characters_type(countries_metdata, country_index):
    return countries_metdata.iat[country_index, HS_DB_CHARACTERS_TYPE_COL_INDEX]


def get_hs_db_records_structure(countries_metdata, country_index):
    return countries_metdata.iat[country_index, HS_DB_RECORDS_STRUCTURE_COL_INDEX]


def get_remarks(countries_metdata, country_index):
    return countries_metdata.iat[country_index, REMARKS_COL_INDEX]


def finish_data_initialization(records):
    return pd.DataFrame(records, columns=COLUMN_NAMES)


def append_country(records, country_name, hs_db_name,
                   hs_db_characters_type=ROMAN_TEXT_LABEL,
                   hs_db_records_structure='FLAT', remarks=''):
    records.append([country_name, hs_db_name, hs_db_characters_type,
                    hs_db_records_structure, remarks])
    return records


def append_countries(records):
    records = append_country(records, 'Afghanistan', 'Afghanistan0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Albania', 'Albania0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Algeria', 'Algeria0.0')
    records = append_country(records, 'Angola', 'Angola0.0')
    records = append_country(records, 'Anguilla', 'Anguilla0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Antigua and Barbuda', 'Antigua and Barbuda0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Argentina', 'Argentina0.0')
    records = append_country(records, 'Armenia', 'Armenia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Aruba', 'Aruba0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Australia', 'Australia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Austria', 'Austria0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Azerbaijan', 'Azerbaijan0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bahamas', 'Bahamas0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bahrain', 'Bahrain0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bangladesh', 'Bangladesh0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Barbados', 'Barbados0.02013', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Belarus', 'Belarus0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Belgium', 'Belgium0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    # records = append_country(records, 'Belize', 'Belize0.0.1', remarks='CORRUPTED')
    records = append_country(records, 'Benin', 'Benin0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bermuda', 'Bermuda0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bhutan', 'Bhutan0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bolivia (Plurinational State of)', 'Bolivia (Plurinational State of)0.0')
    records = append_country(records, 'Bosnia and Herzegovina', 'Bosnia and Herzegovina0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Botswana', 'Botswana0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Brazil', 'Brazil0.0')
    records = append_country(records, 'Brunei Darussalam', 'Brunei Darussalam0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Bulgaria', 'Bulgaria0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Burkina Faso', 'Burkina Faso0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Burundi', 'Burundi0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Cabo Verde', 'Cabo Verde0.02015')
    records = append_country(records, 'Cambodia', 'Cambodia0.02014', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Cameroon', 'Cameroon0.02014')
    records = append_country(records, 'Canada', 'Canada0.0.1', remarks='CORRUPTED')
    records = append_country(records, 'Cayman Islands', 'Cayman Islands0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Central African Republic', 'Central African Republic0.02017')
    records = append_country(records, 'Chad', 'Chad0.02016')
    records = append_country(records, 'Chile', 'Chile0.02017')
    records = append_country(records, 'China', 'China0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Colombia', 'Colombia0.02017')
    records = append_country(records, 'Comoros', 'Comoros0.0')
    records = append_country(records, 'Congo', 'Congo0.02015')
    records = append_country(records, 'Congo (Democratic Republic of)', 'Congo,  Democratic Republic of0.02014')
    records = append_country(records, 'Cook Islands', 'Cook Islands0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Costa Rica', 'Costa Rica0.02016.1', remarks='CORRUPTED')
    records = append_country(records, 'Croatia', 'Croatia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, "Cote d'Ivoire", "C#U00f4te d'Ivoire0.0",
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Cuba', 'Cuba0.02017')
    records = append_country(records, 'Cyprus', 'Cyprus0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Czech Republic', 'Czech Republic0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Denmark', 'Denmark0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Djibouti', 'Djibouti0.02014')
    records = append_country(records, 'Dominica', 'Dominica0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Dominican Republic', 'Dominican Republic0.02017')
    records = append_country(records, 'Ecuador', 'Ecuador0.02017')
    records = append_country(records, 'Egypt', 'Egypt0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'El Salvador', 'El Salvador0.0')
    records = append_country(records, 'Equatorial Guinea', 'Equatorial Guinea0.02007')
    records = append_country(records, 'Eritrea', 'Eritrea0.02006', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Estonia', 'Estonia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Eswatini', 'Eswatini0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Ethiopia', 'Ethiopia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Fiji', 'Fiji0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Finland', 'Finland0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'France', 'France0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'French Polynesia', 'French Polynesia0.0')
    records = append_country(records, 'Gabon', 'Gabon0.02016')
    records = append_country(records, 'Gambia', 'Gambia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Georgia', 'Georgia0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Germany', 'Germany0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Ghana', 'Ghana0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Greece', 'Greece0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Grenada', 'Grenada0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Guatemala', 'Guatemala0.02015')
    records = append_country(records, 'Guinea', 'Guinea0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Guinea-Bissau', 'Guinea-Bissau0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Guyana', 'Guyana0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Haiti', 'Haiti0.02016')
    records = append_country(records, 'Honduras', 'Honduras0.0')
    records = append_country(records, 'Hong Kong,  China Special Administrative Region',
                             'Hong Kong,  China Special Administrative Region0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Hungary', 'Hungary0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Iceland', 'Iceland0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'India', 'India0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Indonesia', 'Indonesia0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Iran (Islamic Republic of)', 'Iran (Islamic Republic of)0.02011',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Ireland', 'Ireland0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Israel', 'Israel0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Italy', 'Italy0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Jamaica', 'Jamaica0.02011', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Japan', 'Japan0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Jordan', 'Jordan0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Kazakhstan', 'Kazakhstan0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Kenya', 'Kenya0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Kiribati', 'Kiribati0.02006', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Korea (Republic of)', 'Korea,  Republic of0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Kosovo', 'Kosovo0.0.1', remarks='CORRUPTED')
    records = append_country(records, 'Kuwait', 'Kuwait0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Kyrgyzstan', 'Kyrgyzstan0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, "Lao (People's Democratic Republic)", "Lao,  People's Democratic Republic0.0",
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Latvia', 'Latvia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Lebanon', 'Lebanon0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Lesotho', 'Lesotho0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Liberia', 'Liberia0.02014', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Libya', 'Libya0.02006', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Liechtenstein', 'Liechtenstein0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Lithuania', 'Lithuania0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Luxembourg', 'Luxembourg0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Macao,  China Special Administrative Region',
                             'Macao,  China Special Administrative Region0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Macedonia (The former Yugoslav Republic of)',
                             'Macedonia,  The former Yugoslav Republic of0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Madagascar', 'Madagascar0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Malawi', 'Malawi0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Malaysia', 'Malaysia0.02014', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Maldives', 'Maldives0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Mali', 'Mali0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Malta', 'Malta0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Mauritania', 'Mauritania0.0')
    records = append_country(records, 'Mauritius', 'Mauritius0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Mayotte', 'Mayotte0.02013')
    records = append_country(records, 'Mexico', 'Mexico0.02017')
    records = append_country(records, 'Micronesia (Federated States of)', 'Micronesia (Federated States of)0.02006',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Moldova (Republic of)', 'Moldova,  Republic of0.02016',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Mongolia', 'Mongolia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Montenegro', 'Montenegro0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Montserrat', 'Montserrat0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Morocco', 'Morocco0.02017')
    records = append_country(records, 'Mozambique', 'Mozambique0.02016')
    records = append_country(records, 'Myanmar', 'Myanmar0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Namibia', 'Namibia0.02018', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Nauru', 'Nauru0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Nepal', 'Nepal0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Netherlands', 'Netherlands0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'New Zealand', 'New Zealand0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Nicaragua', 'Nicaragua0.0')
    records = append_country(records, 'Niger', 'Niger0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Nigeria', 'Nigeria0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Norway', 'Norway0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Oman', 'Oman0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Pakistan', 'Pakistan0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Palau', 'Palau0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Palestine (State of)', 'Palestine,  State of0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Panama', 'Panama0.02013')
    records = append_country(records, 'Papua New Guinea', 'Papua New Guinea0.02010',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Paraguay', 'Paraguay0.0')
    records = append_country(records, 'Peru', 'Peru0.02017')
    records = append_country(records, 'Philippines', 'Philippines0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Poland', 'Poland0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Portugal', 'Portugal0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Qatar', 'Qatar0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Romania', 'Romania0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Russian Federation', 'Russian Federation0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Rwanda', 'Rwanda0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Saint Kitts and Nevis', 'Saint Kitts and Nevis0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Saint Lucia', 'Saint Lucia0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Saint Pierre and Miquelon', 'Saint Pierre and Miquelon0.0')
    records = append_country(records, 'Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Samoa', 'Samoa0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Sao Tome and Principe', 'Sao Tome and Principe0.0')
    records = append_country(records, 'Saudi Arabia', 'Saudi Arabia0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Senegal', 'Senegal0.0', remarks='CORRUPTED')
    records = append_country(records, 'Serbia', 'Serbia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    # records = append_country(records, 'Serbia and Montenegro', 'Serbia & Montenegro0.02005', remarks='CORRUPTED')
    records = append_country(records, 'Seychelles', 'Seychelles0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Sierra Leone', 'Sierra Leone0.02006', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Singapore', 'Singapore0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Slovakia', 'Slovakia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Slovenia', 'Slovenia0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Solomon Islands', 'Solomon Islands0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'South Africa', 'South Africa0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Spain', 'Spain0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Sri Lanka', 'Sri Lanka0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Sudan', 'Sudan0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Suriname', 'Suriname0.02007', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Sweden', 'Sweden0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Switzerland', 'Switzerland0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Syrian Arab Republic', 'Syrian Arab Republic0.02013',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Taipei,  Chinese', 'Taipei,  Chinese0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Tajikistan', 'Tajikistan0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Tanzania (United Republic of)', 'Tanzania,  United Republic of0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Thailand', 'Thailand0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Timor-Leste', 'Timor-Leste0.02016', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Togo', 'Togo0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Tonga', 'Tonga0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Trinidad and Tobago', 'Trinidad and Tobago0.02008',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Tunisia', 'Tunisia0.02015.1', remarks='CORRUPTED')
    records = append_country(records, 'Turkey', 'Turkey0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Tuvalu', 'Tuvalu0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Uganda', 'Uganda0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Ukraine', 'Ukraine0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'United Arab Emirates', 'United Arab Emirates0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'United Kingdom', 'United Kingdom0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'United States of America', 'United States of America0.0',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Uruguay', 'Uruguay0.02017')
    records = append_country(records, 'Uzbekistan', 'Uzbekistan0.02015',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Vanuatu', 'Vanuatu0.02017',
                             hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Venezuela (Bolivarian Republic of)', 'Venezuela (Bolivarian Republic of)0.0')
    records = append_country(records, 'Viet Nam', 'Viet Nam0.0', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Wallis and Futuna', 'Wallis and Futuna0.0')
    records = append_country(records, 'Yemen', 'Yemen0.02017', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Zambia 2013', 'Zambia0.02013', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Zambia 2015', 'Zambia0.02015', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Test country 0', 'Test0', hs_db_characters_type=ENGLISH_TEXT_LABEL,
                             hs_db_records_structure='TREE0')
    records = append_country(records, 'Test country 1', 'Test1', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    records = append_country(records, 'Test country 2', 'Test2', hs_db_characters_type=ENGLISH_TEXT_LABEL)
    return records
