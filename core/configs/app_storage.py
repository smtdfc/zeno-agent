from platformdirs import user_data_dir, user_config_dir, user_cache_dir

appname = "ZenoAgent"
appauthor = "smtdfc"

data_dir = user_data_dir(appname, appauthor)
config_dir = user_config_dir(appname, appauthor)
cache_dir = user_cache_dir(appname, appauthor)
