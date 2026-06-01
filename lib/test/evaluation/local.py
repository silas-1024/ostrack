from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/data/sot/data/got10k_lmdb'
    settings.got10k_path = '/data/sot/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/data/sot/data/itb'
    settings.lasot_extension_subset_path_path = '/data/sot/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/data/sot/data/lasot_lmdb'
    settings.lasot_path = '/data/sot/data/lasot'
    settings.sv248s_test_path = '/media/pc-4090/9bd4d9e0-148f-4dd1-a9c6-1f4c9dff8e4e/datasets/sv248/test_sv'
    settings.sv248s_test_modal_path = '/media/pc-4090/9bd4d9e0-148f-4dd1-a9c6-1f4c9dff8e4e/datasets/sv248/test_sv'
    settings.network_path = '/media/lisuran/ostrack_sv/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/data/sot/data/nfs'
    settings.otb_path = '/data/sot/data/otb'
    settings.prj_dir = '/media/lisuran/OSTrack_sv'
    settings.result_plot_path = '/media/lisuran/OSTrack _sv/output/test/result_plots'
    settings.results_path = '/media/lisuran/OSTrack_sv/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/media/lisuran/OSTrack_sv/output'
    settings.segmentation_path = '/media/lisuran/OSTrack_sv/output/test/segmentation_results'
    settings.tc128_path = '/data/sot/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/data/sot/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/data/sot/data/trackingnet'
    settings.uav_path = '/data/sot/data/uav'
    settings.vot18_path = '/data/sot/data/vot2018'
    settings.vot22_path = '/data/sot/data/vot2022'
    settings.vot_path = '/data/sot/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

