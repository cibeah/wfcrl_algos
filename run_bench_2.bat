python baseline_ippo.py --seed 2 --env_id Dec_WMR_Floris --total_timesteps 5000000
python baseline_ippo.py --seed 2 --env_id Dec_Ablaincourt_Floris --total_timesteps 000000
python baseline_ippo.py --seed 2 --env_id Dec_HornsRev1_Floris --total_timesteps 5000000
python baseline_ippo.py --seed 2 --env_id Dec_Turb3_Row1_Floris --total_timesteps 50000

python baseline_mappo.py --seed 2 --env_id Dec_WMR_Floris --total_timesteps 5000000
python baseline_mappo.py --seed 2 --env_id Dec_Ablaincourt_Floris --total_timesteps 000000
python baseline_mappo.py --seed 2 --env_id Dec_HornsRev1_Floris --total_timesteps 5000000
python baseline_mappo.py --seed 2 --env_id Dec_Turb3_Row1_Floris --total_timesteps 50000

python baseline_ippo_windrose.py --seed 2 --env_id Dec_WMR_Floris --total_timesteps 5000000
python baseline_ippo_windrose.py --seed 2 --env_id Dec_Ablaincourt_Floris --total_timesteps 000000
python baseline_ippo_windrose.py --seed 2 --env_id Dec_HornsRev1_Floris --total_timesteps 5000000
python baseline_ippo_windrose.py --seed 2 --env_id Dec_Turb3_Row1_Floris --total_timesteps 50000 --freq_eval 5

python baseline_mappo_windrose.py --seed 2 --env_id Dec_WMR_Floris --total_timesteps 5000000
python baseline_mappo_windrose.py --seed 2 --env_id Dec_Ablaincourt_Floris --total_timesteps 000000
python baseline_mappo_windrose.py --seed 2 --env_id Dec_HornsRev1_Floris --total_timesteps 5000000
python baseline_mappo_windrose.py --seed 2 --env_id Dec_Turb3_Row1_Floris --total_timesteps 50000 --freq_eval 5