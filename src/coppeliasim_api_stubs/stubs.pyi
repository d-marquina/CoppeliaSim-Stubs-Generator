from typing import Any, List, Dict, Tuple, Callable, Union

class base16:
    """API functions for the `base16` module."""

    # --- Functions ---
    def decode(self, encoded: str) -> bytes:
        """buffer data = base16.decode(string encoded)"""
        ...

    def encode(self, data: bytes) -> str:
        """string encoded = base16.encode(buffer data)"""
        ...


class base64:
    """API functions for the `base64` module."""

    # --- Functions ---
    def decode(self, encoded: str) -> bytes:
        """buffer data = base64.decode(string encoded)"""
        ...

    def encode(self, data: bytes) -> str:
        """string encoded = base64.encode(buffer data)"""
        ...


class checkarg:
    """API functions for the `checkarg` module."""

    # --- Functions ---
    def any(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.any(any value, table opts)"""
        ...

    def bool(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.bool(any value, table opts)"""
        ...

    def float(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.float(any value, table opts)"""
        ...

    def func(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.func(any value, table opts)"""
        ...

    def handle(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.handle(any value, table opts)"""
        ...

    def int(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.int(any value, table opts)"""
        ...

    def object(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.object(any value, table opts)"""
        ...

    def string(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.string(any value, table opts)"""
        ...

    def table(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.table(any value, table opts)"""
        ...

    def union(self, value: Any, opts: dict) -> bool:
        """bool valid = checkarg.union(any value, table opts)"""
        ...


class io:
    """API functions for the `io` module."""

    # --- Functions ---
    def close(self, f: Any) -> None:
        """io.close(file f)"""
        ...

    def flush(self, f: Any) -> None:
        """io.flush(file f)"""
        ...

    def input(self) -> Any:
        """file prev = io.input()"""
        ...

    def lines(self, f: Any) -> Any:
        """function iterator = io.lines(file f)"""
        ...

    def open(self, fileName: str) -> Any:
        """file f = io.open(string fileName)"""
        ...

    def output(self) -> Any:
        """file prev = io.output()"""
        ...

    def read(self, f: Any, format1: str, *args) -> Tuple[str, Any]:
        """string data, ... = io.read(file f, string format1, ...)"""
        ...

    def tmpfile(self) -> Any:
        """file f = io.tmpfile()"""
        ...

    def type(self, f: Any) -> str:
        """string t = io.type(file f)"""
        ...

    def write(self, f: Any, value: Any, *args) -> Tuple[bool, str, int]:
        """bool success, string errorMessage, int errorCode = io.write(file f, any value, ...)"""
        ...


class itertools:
    """API functions for the `itertools` module."""

    # --- Functions ---
    def chain(self, i1: Any, i2: Any, *args) -> Any:
        """function chainedIter = itertools.chain(function i1, function i2, ...)"""
        ...

    def combinations(self, t: dict, length: int) -> dict:
        """table p = itertools.combinations(table t, int length)"""
        ...

    def combinations_with_replacement(self, t: dict, length: int) -> dict:
        """table p = itertools.combinations_with_replacement(table t, int length)"""
        ...

    def ichain(self, i1: Any, i2: Any, *args) -> Any:
        """function chainedIter = itertools.ichain(function i1, function i2, ...)"""
        ...

    def permutations(self, t: dict, length: int) -> dict:
        """table p = itertools.permutations(table t, int length)"""
        ...

    def product(self, table_of_tables: dict) -> dict:
        """table p = itertools.product(table table_of_tables)"""
        ...


class operator:
    """API functions for the `operator` module."""

    # --- Functions ---
    def add(self, a: float, b: float) -> float:
        """number y = operator.add(number a, number b)"""
        ...

    def div(self, a: float, b: float) -> float:
        """number y = operator.div(number a, number b)"""
        ...

    def eq(self, a: float, b: float) -> bool:
        """bool b = operator.eq(number a, number b)"""
        ...

    def ge(self, a: float, b: float) -> bool:
        """bool b = operator.ge(number a, number b)"""
        ...

    def gt(self, a: float, b: float) -> bool:
        """bool b = operator.gt(number a, number b)"""
        ...

    def idiv(self, a: float, b: float) -> float:
        """number y = operator.idiv(number a, number b)"""
        ...

    def land(self, a: float, b: float) -> float:
        """number y = operator.land(number a, number b)"""
        ...

    def le(self, a: float, b: float) -> bool:
        """bool b = operator.le(number a, number b)"""
        ...

    def lor(self, a: float, b: float) -> float:
        """number y = operator.lor(number a, number b)"""
        ...

    def lshl(self, a: float, b: float) -> float:
        """number y = operator.lshl(number a, number b)"""
        ...

    def lshr(self, a: float, b: float) -> float:
        """number y = operator.lshr(number a, number b)"""
        ...

    def lt(self, a: float, b: float) -> bool:
        """bool b = operator.lt(number a, number b)"""
        ...

    def lxor(self, a: float, b: float) -> float:
        """number y = operator.lxor(number a, number b)"""
        ...

    def mod(self, a: float, b: float) -> float:
        """number y = operator.mod(number a, number b)"""
        ...

    def mul(self, a: float, b: float) -> float:
        """number y = operator.mul(number a, number b)"""
        ...

    def neq(self, a: float, b: float) -> bool:
        """bool b = operator.neq(number a, number b)"""
        ...

    def pow(self, a: float, b: float) -> float:
        """number y = operator.pow(number a, number b)"""
        ...

    def sub(self, a: float, b: float) -> float:
        """number y = operator.sub(number a, number b)"""
        ...


class sim:
    """API functions for the `sim` module."""

    # --- Constants ---
    addonscriptcall_cleanup: int
    addonscriptcall_initialization: int
    addonscriptcall_restarting: int
    addonscriptcall_run: int
    addonscriptcall_suspend: int
    api_error_output: int
    api_error_report: int
    api_warning_output: int
    appobj_2delement_type: int
    appobj_collection_type: int
    appobj_collision_type: int
    appobj_distance_type: int
    appobj_ik_type: int
    appobj_object_type: int
    appobj_pathplanning_type: int
    appobj_script_type: int
    appobj_simulation_type: int
    appobj_texture_type: int
    appobj_ui_type: int
    arrayparam_ambient_light: int
    arrayparam_background_color1: int
    arrayparam_background_color2: int
    arrayparam_fog: int
    arrayparam_fog_color: int
    arrayparam_gravity: int
    arrayparam_random_euler: int
    arrayparam_raydirection: int
    arrayparam_rayorigin: int
    banner_backfaceculling: int
    banner_bitmapfont: int
    banner_clickselectsparent: int
    banner_clicktriggersevent: int
    banner_facingcamera: int
    banner_followparentvisibility: int
    banner_fullyfacingcamera: int
    banner_keepsamesize: int
    banner_left: int
    banner_nobackground: int
    banner_overlay: int
    banner_right: int
    boolparam_aux_clip_planes_enabled: int
    boolparam_browser_toolbarbutton_enabled: int
    boolparam_browser_visible: int
    boolparam_calcmodules_toolbarbutton_enabled: int
    boolparam_cansave: int
    boolparam_collision_handling_enabled: int
    boolparam_console_visible: int
    boolparam_display_enabled: int
    boolparam_distance_handling_enabled: int
    boolparam_dynamics_handling_enabled: int
    boolparam_execunsafe: int
    boolparam_execunsafeext: int
    boolparam_exit_request: int
    boolparam_fog_enabled: int
    boolparam_force_calcstruct_all: int
    boolparam_force_calcstruct_all_visible: int
    boolparam_force_show_wireless_emission: int
    boolparam_force_show_wireless_reception: int
    boolparam_full_model_copy_from_api: int
    boolparam_fullscreen: int
    boolparam_gcs_handling_enabled: int
    boolparam_headless: int
    boolparam_hierarchy_toolbarbutton_enabled: int
    boolparam_hierarchy_visible: int
    boolparam_ik_handling_enabled: int
    boolparam_infotext_visible: int
    boolparam_mill_handling_enabled: int
    boolparam_mirrors_enabled: int
    boolparam_objectrotate_toolbarbutton_enabled: int
    boolparam_objectshift_toolbarbutton_enabled: int
    boolparam_objproperties_toolbarbutton_enabled: int
    boolparam_pause_toolbarbutton_enabled: int
    boolparam_play_toolbarbutton_enabled: int
    boolparam_proximity_sensor_handling_enabled: int
    boolparam_rayvalid: int
    boolparam_realtime_simulation: int
    boolparam_rendering_sensor_handling_enabled: int
    boolparam_rml2_available: int
    boolparam_rml4_available: int
    boolparam_rosinterface_donotrunmainscript: int
    boolparam_scene_and_model_load_messages: int
    boolparam_scene_closing: int
    boolparam_shape_textures_are_visible: int
    boolparam_show_w_emitters: int
    boolparam_show_w_receivers: int
    boolparam_statustext_open: int
    boolparam_stop_toolbarbutton_enabled: int
    boolparam_use_glfinish_cmd: int
    boolparam_usingscriptobjects: int
    boolparam_video_recording_triggered: int
    boolparam_vision_sensor_handling_enabled: int
    boolparam_waiting_for_trigger: int
    buffer_base64: int
    buffer_clamp: int
    buffer_double: int
    buffer_float: int
    buffer_int16: int
    buffer_int32: int
    buffer_int8: int
    buffer_split: int
    buffer_uint16: int
    buffer_uint32: int
    buffer_uint8: int
    buffer_uint8argb: int
    buffer_uint8bgr: int
    buffer_uint8rgb: int
    buffer_uint8rgba: int
    bullet_body_angulardamping: int
    bullet_body_autoshrinkconvex: int
    bullet_body_bitcoded: int
    bullet_body_friction: int
    bullet_body_lineardamping: int
    bullet_body_nondefaultcollisionmargingfactor: int
    bullet_body_nondefaultcollisionmargingfactorconvex: int
    bullet_body_oldfriction: int
    bullet_body_restitution: int
    bullet_body_sticky: int
    bullet_body_usenondefaultcollisionmargin: int
    bullet_body_usenondefaultcollisionmarginconvex: int
    bullet_constraintsolvertype_dantzig: int
    bullet_constraintsolvertype_nncg: int
    bullet_constraintsolvertype_projectedgaussseidel: int
    bullet_constraintsolvertype_sequentialimpulse: int
    bullet_global_bitcoded: int
    bullet_global_collisionmarginfactor: int
    bullet_global_computeinertias: int
    bullet_global_constraintsolvertype: int
    bullet_global_constraintsolvingiterations: int
    bullet_global_fullinternalscaling: int
    bullet_global_internalscalingfactor: int
    bullet_global_stepsize: int
    bullet_joint_normalcfm: int
    bullet_joint_pospid1: int
    bullet_joint_pospid2: int
    bullet_joint_pospid3: int
    bullet_joint_stopcfm: int
    bullet_joint_stoperp: int
    buttonproperty_borderless: int
    buttonproperty_button: int
    buttonproperty_closeaction: int
    buttonproperty_downupevent: int
    buttonproperty_editbox: int
    buttonproperty_enabled: int
    buttonproperty_horizontallycentered: int
    buttonproperty_ignoremouse: int
    buttonproperty_isdown: int
    buttonproperty_label: int
    buttonproperty_nobackgroundcolor: int
    buttonproperty_rollupaction: int
    buttonproperty_slider: int
    buttonproperty_staydown: int
    buttonproperty_transparent: int
    buttonproperty_verticallycentered: int
    callbackid_dynstep: int
    callbackid_rossubscriber: int
    callbackid_userdefined: int
    camerafarrayparam_viewfrustum: int
    camerafloatparam_far_clipping: int
    camerafloatparam_near_clipping: int
    camerafloatparam_ortho_size: int
    camerafloatparam_perspective_angle: int
    camerafloatparam_pov_aperture: int
    camerafloatparam_pov_blur_distance: int
    cameraintparam_disabled_light_components: int
    cameraintparam_perspective_operation: int
    cameraintparam_pov_blur_samples: int
    cameraintparam_pov_focal_blur: int
    cameraintparam_rendering_attributes: int
    cameraintparam_trackedobject: int
    childscriptattribute_automaticcascadingcalls: int
    childscriptattribute_enabled: int
    childscriptcall_actuation: int
    childscriptcall_cleanup: int
    childscriptcall_initialization: int
    childscriptcall_sensing: int
    colorcomponent_ambient: int
    colorcomponent_ambient_diffuse: int
    colorcomponent_auxiliary: int
    colorcomponent_diffuse: int
    colorcomponent_emission: int
    colorcomponent_specular: int
    colorcomponent_transparency: int
    customizationscriptattribute_activeduringsimulation: int
    customizationscriptattribute_cleanupbeforesave: int
    customizationscriptcall_aftercopy: int
    customizationscriptcall_beforecopy: int
    customizationscriptcall_cleanup: int
    customizationscriptcall_firstafterinstanceswitch: int
    customizationscriptcall_firstaftersimulation: int
    customizationscriptcall_initialization: int
    customizationscriptcall_lastbeforeinstanceswitch: int
    customizationscriptcall_lastbeforesimulation: int
    customizationscriptcall_nonsimulation: int
    customizationscriptcall_simulationactuation: int
    customizationscriptcall_simulationpause: int
    customizationscriptcall_simulationpausefirst: int
    customizationscriptcall_simulationpauselast: int
    customizationscriptcall_simulationsensing: int
    displayattribute_colorcoded: int
    displayattribute_colorcodedpickpass: int
    displayattribute_colorcodedtriangles: int
    displayattribute_depthpass: int
    displayattribute_dynamiccontentonly: int
    displayattribute_forbidedges: int
    displayattribute_forbidwireframe: int
    displayattribute_forcewireframe: int
    displayattribute_forvisionsensor: int
    displayattribute_ignorelayer: int
    displayattribute_ignorerenderableflag: int
    displayattribute_mainselection: int
    displayattribute_mirror: int
    displayattribute_nodrawingobjects: int
    displayattribute_noghosts: int
    displayattribute_noopenglcallbacks: int
    displayattribute_noparticles: int
    displayattribute_nopointclouds: int
    displayattribute_originalcolors: int
    displayattribute_pickpass: int
    displayattribute_renderpass: int
    displayattribute_selected: int
    displayattribute_thickEdges: int
    displayattribute_trianglewireframe: int
    displayattribute_useauxcomponent: int
    distcalcmethod_dac: int
    distcalcmethod_dac_if_nonzero: int
    distcalcmethod_dl: int
    distcalcmethod_dl_and_dac: int
    distcalcmethod_dl_if_nonzero: int
    distcalcmethod_max_dl_dac: int
    distcalcmethod_sqrt_dl2_and_dac2: int
    dlgret_cancel: int
    dlgret_no: int
    dlgret_ok: int
    dlgret_still_open: int
    dlgret_yes: int
    dlgstyle_dont_center: int
    dlgstyle_input: int
    dlgstyle_message: int
    dlgstyle_ok: int
    dlgstyle_ok_cancel: int
    dlgstyle_yes_no: int
    drawing_12percenttransparency: int
    drawing_25percenttransparency: int
    drawing_50percenttransparency: int
    drawing_auxchannelcolor1: int
    drawing_auxchannelcolor2: int
    drawing_backfaceculling: int
    drawing_cubepoints: int
    drawing_cubepts: int
    drawing_cyclic: int
    drawing_discpoints: int
    drawing_discpts: int
    drawing_emissioncolor: int
    drawing_facingcamera: int
    drawing_followparentvisibility: int
    drawing_itemcolors: int
    drawing_itemsizes: int
    drawing_itemtransparency: int
    drawing_lines: int
    drawing_linestrip: int
    drawing_local: int
    drawing_overlay: int
    drawing_painttag: int
    drawing_persistent: int
    drawing_points: int
    drawing_quadpoints: int
    drawing_quadpts: int
    drawing_spherepoints: int
    drawing_spherepts: int
    drawing_trianglepoints: int
    drawing_trianglepts: int
    drawing_triangles: int
    drawing_vertexcolors: int
    drawing_wireframe: int
    dummy_linktype_dynamics_force_constraint: int
    dummy_linktype_dynamics_loop_closure: int
    dummy_linktype_gcs_loop_closure: int
    dummy_linktype_gcs_target: int
    dummy_linktype_gcs_tip: int
    dummy_linktype_ik_tip_target: int
    dummyfloatparam_follow_path_offset: int
    dummyfloatparam_size: int
    dummyintparam_dummytype: int
    dummyintparam_follow_path: int
    dummyintparam_link_type: int
    dummylink_dynloopclosure: int
    dummylink_dyntendon: int
    dummystringparam_assemblytag: int
    dummytype_assembly: int
    dummytype_default: int
    dummytype_dynloopclosure: int
    dummytype_dyntendon: int
    dynmat_default: int
    dynmat_floor: int
    dynmat_foot: int
    dynmat_gripper: int
    dynmat_highfriction: int
    dynmat_lowfriction: int
    dynmat_nofriction: int
    dynmat_reststackgrasp: int
    dynmat_wheel: int
    filedlg_type_folder: int
    filedlg_type_load: int
    filedlg_type_load_multiple: int
    filedlg_type_save: int
    filtercomponent_3x3filter: int
    filtercomponent_5x5filter: int
    filtercomponent_addbuffer1: int
    filtercomponent_addtobuffer1: int
    filtercomponent_binary: int
    filtercomponent_blobextraction: int
    filtercomponent_circularcut: int
    filtercomponent_colorsegmentation: int
    filtercomponent_correlationwithbuffer1: int
    filtercomponent_customized: int
    filtercomponent_edge: int
    filtercomponent_frombuffer1: int
    filtercomponent_frombuffer2: int
    filtercomponent_horizontalflip: int
    filtercomponent_imagetocoord: int
    filtercomponent_intensityscale: int
    filtercomponent_keeporremovecolors: int
    filtercomponent_multiplywithbuffer1: int
    filtercomponent_normalize: int
    filtercomponent_originaldepth: int
    filtercomponent_originalimage: int
    filtercomponent_pixelchange: int
    filtercomponent_rectangularcut: int
    filtercomponent_resize: int
    filtercomponent_rotate: int
    filtercomponent_scaleandoffsetcolors: int
    filtercomponent_sharpen: int
    filtercomponent_shift: int
    filtercomponent_subtractbuffer1: int
    filtercomponent_subtractfrombuffer1: int
    filtercomponent_swapbuffers: int
    filtercomponent_swapwithbuffer1: int
    filtercomponent_tobuffer1: int
    filtercomponent_tobuffer2: int
    filtercomponent_todepthoutput: int
    filtercomponent_tooutput: int
    filtercomponent_uniformimage: int
    filtercomponent_velodyne: int
    filtercomponent_verticalflip: int
    floatparam_dynamic_step_size: int
    floatparam_maxtrisizeabs: int
    floatparam_mintrisizerel: int
    floatparam_mouse_wheel_zoom_factor: int
    floatparam_physicstimestep: int
    floatparam_rand: int
    floatparam_simulation_time_step: int
    floatparam_stereo_distance: int
    forcefloatparam_error_a: int
    forcefloatparam_error_angle: int
    forcefloatparam_error_b: int
    forcefloatparam_error_g: int
    forcefloatparam_error_pos: int
    forcefloatparam_error_x: int
    forcefloatparam_error_y: int
    forcefloatparam_error_z: int
    graphintparam_needs_refresh: int
    handle_all: int
    handle_all_except_explicit: int
    handle_all_except_self: int
    handle_app: int
    handle_appstorage: int
    handle_chain: int
    handle_default: int
    handle_inverse: int
    handle_main_script: int
    handle_mainscript: int
    handle_mesh: int
    handle_parent: int
    handle_sandbox: int
    handle_scene: int
    handle_sceneobject: int
    handle_self: int
    handle_single: int
    handle_tree: int
    handle_world: int
    handleflag_abscoords: int
    handleflag_addmultiple: int
    handleflag_altname: int
    handleflag_assembly: int
    handleflag_axis: int
    handleflag_camera: int
    handleflag_codedstring: int
    handleflag_depthbuffer: int
    handleflag_depthbuffermeters: int
    handleflag_extended: int
    handleflag_greyscale: int
    handleflag_keeporiginal: int
    handleflag_model: int
    handleflag_rawvalue: int
    handleflag_reljointbaseframe: int
    handleflag_resetforce: int
    handleflag_resetforcetorque: int
    handleflag_resettorque: int
    handleflag_setmultiple: int
    handleflag_silenterror: int
    handleflag_togglevisibility: int
    handleflag_wxyzquat: int
    ik_alpha_beta_constraint: int
    ik_damped_least_squares_method: int
    ik_gamma_constraint: int
    ik_jacobian_transpose_method: int
    ik_pseudo_inverse_method: int
    ik_undamped_pseudo_inverse_method: int
    ik_x_constraint: int
    ik_y_constraint: int
    ik_z_constraint: int
    ikresult_fail: int
    ikresult_not_performed: int
    ikresult_success: int
    imgcomb_horizontal: int
    imgcomb_vertical: int
    intparam_compilation_version: int
    intparam_core_count: int
    intparam_current_page: int
    intparam_dlgverbosity: int
    intparam_dynamic_engine: int
    intparam_dynamic_iteration_count: int
    intparam_dynamic_step_divider: int
    intparam_dynamic_warning_disabled_mask: int
    intparam_edit_mode_type: int
    intparam_error_report_mode: int
    intparam_exitcode: int
    intparam_flymode_camera_handle: int
    intparam_hierarchychangecounter: int
    intparam_idle_fps: int
    intparam_infotext_style: int
    intparam_motionplanning_seed: int
    intparam_mouse_buttons: int
    intparam_mouse_x: int
    intparam_mouse_y: int
    intparam_mouseclickcounterdown: int
    intparam_mouseclickcounterup: int
    intparam_notifydeprecated: int
    intparam_objectcreationcounter: int
    intparam_objectdestructioncounter: int
    intparam_platform: int
    intparam_processcnt: int
    intparam_processid: int
    intparam_program_full_version: int
    intparam_program_revision: int
    intparam_program_version: int
    intparam_prox_sensor_select_down: int
    intparam_prox_sensor_select_up: int
    intparam_qt_version: int
    intparam_scene_index: int
    intparam_scene_unique_id: int
    intparam_server_port_next: int
    intparam_server_port_range: int
    intparam_server_port_start: int
    intparam_settings: int
    intparam_simulation_warning_disabled_mask: int
    intparam_speedmodifier: int
    intparam_statusbarverbosity: int
    intparam_stop_request_counter: int
    intparam_verbosity: int
    intparam_videoencoderindex: int
    intparam_visible_layers: int
    intparam_work_thread_calc_time_ms: int
    intparam_work_thread_count: int
    joint_prismatic: int
    joint_prismatic_subtype: int
    joint_revolute: int
    joint_revolute_subtype: int
    joint_spherical: int
    joint_spherical_subtype: int
    jointdynctrl_callback: int
    jointdynctrl_force: int
    jointdynctrl_free: int
    jointdynctrl_position: int
    jointdynctrl_spring: int
    jointdynctrl_velocity: int
    jointfloatparam_error_a: int
    jointfloatparam_error_angle: int
    jointfloatparam_error_b: int
    jointfloatparam_error_g: int
    jointfloatparam_error_pos: int
    jointfloatparam_error_x: int
    jointfloatparam_error_y: int
    jointfloatparam_error_z: int
    jointfloatparam_ik_weight: int
    jointfloatparam_intrinsic_qw: int
    jointfloatparam_intrinsic_qx: int
    jointfloatparam_intrinsic_qy: int
    jointfloatparam_intrinsic_qz: int
    jointfloatparam_intrinsic_x: int
    jointfloatparam_intrinsic_y: int
    jointfloatparam_intrinsic_z: int
    jointfloatparam_kc_c: int
    jointfloatparam_kc_k: int
    jointfloatparam_maxaccel: int
    jointfloatparam_maxjerk: int
    jointfloatparam_maxvel: int
    jointfloatparam_pid_d: int
    jointfloatparam_pid_i: int
    jointfloatparam_pid_p: int
    jointfloatparam_screw_pitch: int
    jointfloatparam_screwlead: int
    jointfloatparam_spherical_qw: int
    jointfloatparam_spherical_qx: int
    jointfloatparam_spherical_qy: int
    jointfloatparam_spherical_qz: int
    jointfloatparam_step_size: int
    jointfloatparam_upper_limit: int
    jointfloatparam_velocity: int
    jointfloatparam_vortex_dep_multiplication: int
    jointfloatparam_vortex_dep_offset: int
    jointintparam_ctrl_enabled: int
    jointintparam_dynctrlmode: int
    jointintparam_dynposctrltype: int
    jointintparam_dynvelctrltype: int
    jointintparam_motor_enabled: int
    jointintparam_velocity_lock: int
    jointintparam_vortex_dep_handle: int
    jointmode_dependent: int
    jointmode_dynamic: int
    jointmode_force: int
    jointmode_ik: int
    jointmode_ikdependent: int
    jointmode_kinematic: int
    jointmode_passive: int
    light_directional: int
    light_directional_subtype: int
    light_omnidirectional: int
    light_omnidirectional_subtype: int
    light_spot: int
    light_spot_subtype: int
    lightfloatparam_const_attenuation: int
    lightfloatparam_lin_attenuation: int
    lightfloatparam_quad_attenuation: int
    lightfloatparam_spot_cutoff: int
    lightfloatparam_spot_exponent: int
    lightintparam_pov_casts_shadows: int
    mainscriptcall_cleanup: int
    mainscriptcall_initialization: int
    mainscriptcall_regular: int
    message_bannerclicked: int
    message_keypress: int
    message_model_loaded: int
    message_object_selection_changed: int
    message_pick_select_down: int
    message_prox_sensor_select_down: int
    message_prox_sensor_select_up: int
    message_scene_loaded: int
    message_ui_button_state_change: int
    mill_cone_subtype: int
    mill_cylinder_subtype: int
    mill_disc_subtype: int
    mill_pyramid_subtype: int
    millintparam_volume_type: int
    mirrorfloatparam_height: int
    mirrorfloatparam_reflectance: int
    mirrorfloatparam_width: int
    mirrorintparam_enable: int
    modelproperty_not_collidable: int
    modelproperty_not_detectable: int
    modelproperty_not_dynamic: int
    modelproperty_not_measurable: int
    modelproperty_not_model: int
    modelproperty_not_renderable: int
    modelproperty_not_reset: int
    modelproperty_not_respondable: int
    modelproperty_not_showasinsidemodel: int
    modelproperty_not_visible: int
    modelproperty_scripts_inactive: int
    moduleinfo_builddatestr: int
    moduleinfo_extversionint: int
    moduleinfo_extversionstr: int
    moduleinfo_statusbarverbosity: int
    moduleinfo_verbosity: int
    msgbox_buttons_ok: int
    msgbox_buttons_okcancel: int
    msgbox_buttons_yesno: int
    msgbox_buttons_yesnocancel: int
    msgbox_return_cancel: int
    msgbox_return_error: int
    msgbox_return_no: int
    msgbox_return_ok: int
    msgbox_return_yes: int
    msgbox_type_critical: int
    msgbox_type_info: int
    msgbox_type_question: int
    msgbox_type_warning: int
    mujoco_body_condim: int
    mujoco_body_friction1: int
    mujoco_body_friction2: int
    mujoco_body_friction3: int
    mujoco_body_margin: int
    mujoco_body_priority: int
    mujoco_body_solimp1: int
    mujoco_body_solimp2: int
    mujoco_body_solimp3: int
    mujoco_body_solimp4: int
    mujoco_body_solimp5: int
    mujoco_body_solmix: int
    mujoco_body_solref1: int
    mujoco_body_solref2: int
    mujoco_dummy_bitcoded: int
    mujoco_dummy_damping: int
    mujoco_dummy_limited: int
    mujoco_dummy_margin: int
    mujoco_dummy_proxyjointid: int
    mujoco_dummy_range1: int
    mujoco_dummy_range2: int
    mujoco_dummy_solimplimit1: int
    mujoco_dummy_solimplimit2: int
    mujoco_dummy_solimplimit3: int
    mujoco_dummy_solimplimit4: int
    mujoco_dummy_solimplimit5: int
    mujoco_dummy_solreflimit1: int
    mujoco_dummy_solreflimit2: int
    mujoco_dummy_springlength: int
    mujoco_dummy_stiffness: int
    mujoco_global_balanceinertias: int
    mujoco_global_bitcoded: int
    mujoco_global_boundinertia: int
    mujoco_global_boundmass: int
    mujoco_global_computeinertias: int
    mujoco_global_cone: int
    mujoco_global_density: int
    mujoco_global_impratio: int
    mujoco_global_integrator: int
    mujoco_global_iterations: int
    mujoco_global_kininertia: int
    mujoco_global_kinmass: int
    mujoco_global_multiccd: int
    mujoco_global_multithreaded: int
    mujoco_global_nconmax: int
    mujoco_global_njmax: int
    mujoco_global_nstack: int
    mujoco_global_overridecontacts: int
    mujoco_global_overridekin: int
    mujoco_global_overridemargin: int
    mujoco_global_overridesolimp1: int
    mujoco_global_overridesolimp2: int
    mujoco_global_overridesolimp3: int
    mujoco_global_overridesolimp4: int
    mujoco_global_overridesolimp5: int
    mujoco_global_overridesolref1: int
    mujoco_global_overridesolref2: int
    mujoco_global_rebuildtrigger: int
    mujoco_global_solver: int
    mujoco_global_viscosity: int
    mujoco_global_wind1: int
    mujoco_global_wind2: int
    mujoco_global_wind3: int
    mujoco_joint_armature: int
    mujoco_joint_damping: int
    mujoco_joint_dependentobjectid: int
    mujoco_joint_frictionloss: int
    mujoco_joint_margin: int
    mujoco_joint_polycoef1: int
    mujoco_joint_polycoef2: int
    mujoco_joint_polycoef3: int
    mujoco_joint_polycoef4: int
    mujoco_joint_polycoef5: int
    mujoco_joint_pospid1: int
    mujoco_joint_pospid2: int
    mujoco_joint_pospid3: int
    mujoco_joint_solimpfriction1: int
    mujoco_joint_solimpfriction2: int
    mujoco_joint_solimpfriction3: int
    mujoco_joint_solimpfriction4: int
    mujoco_joint_solimpfriction5: int
    mujoco_joint_solimplimit1: int
    mujoco_joint_solimplimit2: int
    mujoco_joint_solimplimit3: int
    mujoco_joint_solimplimit4: int
    mujoco_joint_solimplimit5: int
    mujoco_joint_solreffriction1: int
    mujoco_joint_solreffriction2: int
    mujoco_joint_solreflimit1: int
    mujoco_joint_solreflimit2: int
    mujoco_joint_springdamper1: int
    mujoco_joint_springdamper2: int
    mujoco_joint_springref: int
    mujoco_joint_stiffness: int
    navigation_cameraangle: int
    navigation_camerafly: int
    navigation_camerarotate: int
    navigation_camerarotatemiddlebutton: int
    navigation_camerarotaterightbutton: int
    navigation_camerashift: int
    navigation_cameratilt: int
    navigation_camerazoom: int
    navigation_camerazoomwheel: int
    navigation_clickselection: int
    navigation_createpathpoint: int
    navigation_ctrlselection: int
    navigation_objectrotate: int
    navigation_objectshift: int
    navigation_passive: int
    navigation_shiftselection: int
    newton_body_angulardrag: int
    newton_body_bitcoded: int
    newton_body_fastmoving: int
    newton_body_kineticfriction: int
    newton_body_lineardrag: int
    newton_body_restitution: int
    newton_body_staticfriction: int
    newton_global_bitcoded: int
    newton_global_computeinertias: int
    newton_global_constraintsolvingiterations: int
    newton_global_contactmergetolerance: int
    newton_global_exactsolver: int
    newton_global_highjointaccuracy: int
    newton_global_multithreading: int
    newton_global_stepsize: int
    newton_joint_dependencyfactor: int
    newton_joint_dependencyoffset: int
    newton_joint_dependentobjectid: int
    newton_joint_objectid: int
    newton_joint_pospid1: int
    newton_joint_pospid2: int
    newton_joint_pospid3: int
    object_camera_type: int
    object_dummy_type: int
    object_forcesensor_type: int
    object_graph_type: int
    object_joint_type: int
    object_light_type: int
    object_mill_type: int
    object_mirror_type: int
    object_no_subtype: int
    object_octree_type: int
    object_path_type: int
    object_pointcloud_type: int
    object_proximitysensor_type: int
    object_renderingsensor_type: int
    object_script_type: int
    object_shape_type: int
    object_visionsensor_type: int
    objectproperty_cannotdelete: int
    objectproperty_cannotdeleteduringsim: int
    objectproperty_canupdatedna: int
    objectproperty_collapsed: int
    objectproperty_depthinvisible: int
    objectproperty_dontshowasinsidemodel: int
    objectproperty_hiddenforsimulation: int
    objectproperty_hierarchyhiddenmodelchild: int
    objectproperty_ignoreviewfitting: int
    objectproperty_selectable: int
    objectproperty_selectinvisible: int
    objectproperty_selectmodelbaseinstead: int
    objectspecialproperty_collidable: int
    objectspecialproperty_detectable: int
    objectspecialproperty_detectable_all: int
    objectspecialproperty_detectable_capacitive: int
    objectspecialproperty_detectable_inductive: int
    objectspecialproperty_detectable_infrared: int
    objectspecialproperty_detectable_laser: int
    objectspecialproperty_detectable_ultrasonic: int
    objectspecialproperty_measurable: int
    objectspecialproperty_pathplanning_ignored: int
    objectspecialproperty_renderable: int
    objecttype_collection: int
    objecttype_interfacestack: int
    objecttype_mesh: int
    objecttype_sceneobject: int
    objecttype_script: int
    objecttype_texture: int
    objfloatparam_abs_rot_velocity: int
    objfloatparam_abs_x_velocity: int
    objfloatparam_abs_y_velocity: int
    objfloatparam_abs_z_velocity: int
    objfloatparam_modelbbox_max_x: int
    objfloatparam_modelbbox_max_y: int
    objfloatparam_modelbbox_max_z: int
    objfloatparam_modelbbox_min_x: int
    objfloatparam_modelbbox_min_y: int
    objfloatparam_modelbbox_min_z: int
    objfloatparam_objbbox_max_x: int
    objfloatparam_objbbox_max_y: int
    objfloatparam_objbbox_max_z: int
    objfloatparam_objbbox_min_x: int
    objfloatparam_objbbox_min_y: int
    objfloatparam_objbbox_min_z: int
    objfloatparam_size_factor: int
    objfloatparam_transparency_offset: int
    objintparam_child_role: int
    objintparam_collection_self_collision_indicator: int
    objintparam_hierarchycolor: int
    objintparam_illumination_handle: int
    objintparam_manipulation_permissions: int
    objintparam_parent_role: int
    objintparam_unique_id: int
    objintparam_visibility_layer: int
    objintparam_visible: int
    objstringparam_dna: int
    objstringparam_unique_id: int
    octreefloatparam_voxelsize: int
    ode_body_angulardamping: int
    ode_body_friction: int
    ode_body_lineardamping: int
    ode_body_maxcontacts: int
    ode_body_softcfm: int
    ode_body_softerp: int
    ode_global_bitcoded: int
    ode_global_cfm: int
    ode_global_computeinertias: int
    ode_global_constraintsolvingiterations: int
    ode_global_erp: int
    ode_global_fullinternalscaling: int
    ode_global_internalscalingfactor: int
    ode_global_quickstep: int
    ode_global_randomseed: int
    ode_global_stepsize: int
    ode_joint_bounce: int
    ode_joint_fudgefactor: int
    ode_joint_normalcfm: int
    ode_joint_pospid1: int
    ode_joint_pospid2: int
    ode_joint_pospid3: int
    ode_joint_stopcfm: int
    ode_joint_stoperp: int
    particle_cyclic: int
    particle_emissioncolor: int
    particle_ignoresgravity: int
    particle_invisible: int
    particle_itemcolors: int
    particle_itemdensities: int
    particle_itemsizes: int
    particle_painttag: int
    particle_particlerespondable: int
    particle_points1: int
    particle_points2: int
    particle_points4: int
    particle_respondable1to4: int
    particle_respondable5to8: int
    particle_roughspheres: int
    particle_spheres: int
    particle_water: int
    pathproperty_automatic_orientation: int
    pathproperty_closed_path: int
    pathproperty_flat_path: int
    pathproperty_keep_x_up: int
    pathproperty_show_line: int
    pathproperty_show_orientation: int
    pathproperty_show_position: int
    physics_bullet: int
    physics_drake: int
    physics_mujoco: int
    physics_newton: int
    physics_ode: int
    physics_vortex: int
    plugininfo_builddatestr: int
    plugininfo_extversionint: int
    plugininfo_extversionstr: int
    plugininfo_statusbarverbosity: int
    plugininfo_verbosity: int
    primitiveshape_capsule: int
    primitiveshape_cone: int
    primitiveshape_cuboid: int
    primitiveshape_cylinder: int
    primitiveshape_disc: int
    primitiveshape_heightfield: int
    primitiveshape_none: int
    primitiveshape_plane: int
    primitiveshape_spheroid: int
    propertyinfo_deprecated: int
    propertyinfo_largedata: int
    propertyinfo_modelhashexclude: int
    propertyinfo_notreadable: int
    propertyinfo_notwritable: int
    propertyinfo_removable: int
    propertytype_bool: int
    propertytype_buffer: int
    propertytype_color: int
    propertytype_float: int
    propertytype_floatarray: int
    propertytype_int: int
    propertytype_intarray: int
    propertytype_intarray2: int
    propertytype_long: int
    propertytype_matrix3x3: int
    propertytype_matrix4x4: int
    propertytype_pose: int
    propertytype_quaternion: int
    propertytype_string: int
    propertytype_table: int
    propertytype_vector2: int
    propertytype_vector3: int
    proximitysensor_cone: int
    proximitysensor_cone_subtype: int
    proximitysensor_cylinder: int
    proximitysensor_cylinder_subtype: int
    proximitysensor_disc: int
    proximitysensor_disc_subtype: int
    proximitysensor_pyramid: int
    proximitysensor_pyramid_subtype: int
    proximitysensor_ray: int
    proximitysensor_ray_subtype: int
    proxintparam_entity_to_detect: int
    proxintparam_ray_invisibility: int
    proxintparam_volume_type: int
    pure_primitive_cone: int
    pure_primitive_cuboid: int
    pure_primitive_cylinder: int
    pure_primitive_disc: int
    pure_primitive_heightfield: int
    pure_primitive_none: int
    pure_primitive_plane: int
    pure_primitive_spheroid: int
    rml_disable_extremum_motion_states_calc: int
    rml_keep_current_vel_if_fallback_strategy: int
    rml_keep_target_vel: int
    rml_no_sync: int
    rml_only_phase_sync: int
    rml_only_time_sync: int
    rml_phase_sync_if_possible: int
    rml_recompute_trajectory: int
    ruckig_minaccel: int
    ruckig_minvel: int
    ruckig_nosync: int
    ruckig_phasesync: int
    ruckig_timesync: int
    sceneobject_camera: int
    sceneobject_dummy: int
    sceneobject_forcesensor: int
    sceneobject_graph: int
    sceneobject_joint: int
    sceneobject_light: int
    sceneobject_mill: int
    sceneobject_mirror: int
    sceneobject_octree: int
    sceneobject_path: int
    sceneobject_pointcloud: int
    sceneobject_proximitysensor: int
    sceneobject_renderingsensor: int
    sceneobject_script: int
    sceneobject_shape: int
    sceneobject_visionsensor: int
    script_call_error: int
    script_lua_error: int
    script_main_not_called: int
    script_main_script_nonexistent: int
    script_no_error: int
    script_reentrance_error: int
    scriptattribute_debuglevel: int
    scriptattribute_enabled: int
    scriptattribute_executioncount: int
    scriptattribute_executionorder: int
    scriptattribute_scripthandle: int
    scriptattribute_scripttype: int
    scriptdebug_allcalls: int
    scriptdebug_callsandvars: int
    scriptdebug_none: int
    scriptdebug_syscalls: int
    scriptdebug_vars: int
    scriptdebug_vars_interval: int
    scriptexecorder_first: int
    scriptexecorder_last: int
    scriptexecorder_normal: int
    scriptintparam_autorestartonerror: int
    scriptintparam_enabled: int
    scriptintparam_execcount: int
    scriptintparam_execorder: int
    scriptintparam_handle: int
    scriptintparam_lang: int
    scriptintparam_objecthandle: int
    scriptintparam_type: int
    scriptstringparam_description: int
    scriptstringparam_lang: int
    scriptstringparam_name: int
    scriptstringparam_nameext: int
    scriptstringparam_text: int
    scriptthreadresume_actuation_first: int
    scriptthreadresume_actuation_last: int
    scriptthreadresume_allnotyetresumed: int
    scriptthreadresume_custom: int
    scriptthreadresume_default: int
    scriptthreadresume_sensing_first: int
    scriptthreadresume_sensing_last: int
    scripttype_addon: int
    scripttype_addonfunction: int
    scripttype_addonscript: int
    scripttype_childscript: int
    scripttype_customization: int
    scripttype_customizationscript: int
    scripttype_main: int
    scripttype_mainscript: int
    scripttype_passive: int
    scripttype_sandbox: int
    scripttype_sandboxscript: int
    scripttype_simulation: int
    scripttype_threaded: int
    shape_compound: int
    shape_multishape_subtype: int
    shape_simple: int
    shape_simpleshape_subtype: int
    shapefloatparam_edge_angle: int
    shapefloatparam_init_ang_velocity_x: int
    shapefloatparam_init_ang_velocity_y: int
    shapefloatparam_init_ang_velocity_z: int
    shapefloatparam_init_velocity_a: int
    shapefloatparam_init_velocity_b: int
    shapefloatparam_init_velocity_g: int
    shapefloatparam_init_velocity_x: int
    shapefloatparam_init_velocity_y: int
    shapefloatparam_init_velocity_z: int
    shapefloatparam_mass: int
    shapefloatparam_shading_angle: int
    shapefloatparam_texture_a: int
    shapefloatparam_texture_b: int
    shapefloatparam_texture_g: int
    shapefloatparam_texture_scaling_x: int
    shapefloatparam_texture_scaling_y: int
    shapefloatparam_texture_x: int
    shapefloatparam_texture_y: int
    shapefloatparam_texture_z: int
    shapeintparam_component_cnt: int
    shapeintparam_compound: int
    shapeintparam_convex: int
    shapeintparam_convex_check: int
    shapeintparam_culling: int
    shapeintparam_edge_borders_hidden: int
    shapeintparam_edge_visibility: int
    shapeintparam_kinematic: int
    shapeintparam_respondable: int
    shapeintparam_respondable_mask: int
    shapeintparam_respondablesuspendcnt: int
    shapeintparam_sleepmodestart: int
    shapeintparam_static: int
    shapeintparam_wireframe: int
    shapestringparam_color_name: int
    shapestringparam_colorname: int
    sim_lang_lua: int
    sim_lang_python: int
    sim_lang_undefined: int
    simulation_advancing: int
    simulation_advancing_abouttostop: int
    simulation_advancing_firstafterpause: int
    simulation_advancing_firstafterstop: int
    simulation_advancing_lastbeforepause: int
    simulation_advancing_lastbeforestop: int
    simulation_advancing_running: int
    simulation_paused: int
    simulation_stopped: int
    stream_transf_cumulative: int
    stream_transf_derivative: int
    stream_transf_integral: int
    stream_transf_raw: int
    stringparam_additionalpythonpath: int
    stringparam_addondir: int
    stringparam_addonpath: int
    stringparam_app_arg1: int
    stringparam_app_arg2: int
    stringparam_app_arg3: int
    stringparam_app_arg4: int
    stringparam_app_arg5: int
    stringparam_app_arg6: int
    stringparam_app_arg7: int
    stringparam_app_arg8: int
    stringparam_app_arg9: int
    stringparam_application_path: int
    stringparam_datadir: int
    stringparam_defaultpython: int
    stringparam_dlgverbosity: int
    stringparam_importexportdir: int
    stringparam_legacymachinetag: int
    stringparam_logfilter: int
    stringparam_luadir: int
    stringparam_machine_id: int
    stringparam_machine_id_legacy: int
    stringparam_modeldefaultdir: int
    stringparam_mujocodir: int
    stringparam_pythondir: int
    stringparam_remoteapi_temp_file_dir: int
    stringparam_resourcesdir: int
    stringparam_sandboxlang: int
    stringparam_scene_name: int
    stringparam_scene_path: int
    stringparam_scene_path_and_name: int
    stringparam_scene_unique_id: int
    stringparam_scenedefaultdir: int
    stringparam_statusbarverbosity: int
    stringparam_systemdir: int
    stringparam_tempdir: int
    stringparam_tempscenedir: int
    stringparam_uniqueid: int
    stringparam_usersettingsdir: int
    stringparam_verbosity: int
    stringparam_video_filename: int
    syscb_actuation: int
    syscb_aftercopy: int
    syscb_aftercreate: int
    syscb_afterdelete: int
    syscb_afterinstanceswitch: int
    syscb_aftersimulation: int
    syscb_aos_resume: int
    syscb_aos_run: int
    syscb_aos_suspend: int
    syscb_beforecopy: int
    syscb_beforedelete: int
    syscb_beforeinstanceswitch: int
    syscb_beforemainscript: int
    syscb_beforesimulation: int
    syscb_cleanup: int
    syscb_contact: int
    syscb_contactcallback: int
    syscb_customcallback1: int
    syscb_customcallback2: int
    syscb_customcallback3: int
    syscb_customcallback4: int
    syscb_data: int
    syscb_dyn: int
    syscb_dyncallback: int
    syscb_init: int
    syscb_joint: int
    syscb_jointcallback: int
    syscb_moduleentry: int
    syscb_nonsimulation: int
    syscb_regular: int
    syscb_resume: int
    syscb_selchange: int
    syscb_sensing: int
    syscb_suspend: int
    syscb_suspended: int
    syscb_thread: int
    syscb_trigger: int
    syscb_userconfig: int
    syscb_vision: int
    texturemap_cube: int
    texturemap_cylinder: int
    texturemap_plane: int
    texturemap_sphere: int
    verbosity_debug: int
    verbosity_default: int
    verbosity_errors: int
    verbosity_infos: int
    verbosity_loadinfos: int
    verbosity_msgs: int
    verbosity_none: int
    verbosity_once: int
    verbosity_onlyterminal: int
    verbosity_questions: int
    verbosity_scripterrors: int
    verbosity_scriptinfos: int
    verbosity_scriptwarnings: int
    verbosity_trace: int
    verbosity_traceall: int
    verbosity_tracelua: int
    verbosity_undecorated: int
    verbosity_useglobal: int
    verbosity_warnings: int
    visionfarrayparam_viewfrustum: int
    visionfloatparam_far_clipping: int
    visionfloatparam_near_clipping: int
    visionfloatparam_ortho_size: int
    visionfloatparam_perspective_angle: int
    visionfloatparam_pov_aperture: int
    visionfloatparam_pov_blur_distance: int
    visionintparam_depthignored: int
    visionintparam_disabled_light_components: int
    visionintparam_entity_to_render: int
    visionintparam_perspective_operation: int
    visionintparam_pov_blur_sampled: int
    visionintparam_pov_focal_blur: int
    visionintparam_render_mode: int
    visionintparam_rendering_attributes: int
    visionintparam_resolution_x: int
    visionintparam_resolution_y: int
    visionintparam_rgbignored: int
    visionintparam_windowed_pos_x: int
    visionintparam_windowed_pos_y: int
    visionintparam_windowed_size_x: int
    visionintparam_windowed_size_y: int
    volume_cone: int
    volume_cylinder: int
    volume_disc: int
    volume_pyramid: int
    volume_randomizedray: int
    volume_ray: int
    vortex_body_adhesiveforce: int
    vortex_body_angularvelocitydamping: int
    vortex_body_autoangulardamping: int
    vortex_body_autoangulardampingtensionratio: int
    vortex_body_autosleepangularaccelthreshold: int
    vortex_body_autosleepangularspeedthreshold: int
    vortex_body_autosleeplinearaccelthreshold: int
    vortex_body_autosleeplinearspeedthreshold: int
    vortex_body_autosleepsteplivethreshold: int
    vortex_body_autoslip: int
    vortex_body_bitcoded: int
    vortex_body_compliance: int
    vortex_body_convexshapesasrandom: int
    vortex_body_damping: int
    vortex_body_fastmoving: int
    vortex_body_linearvelocitydamping: int
    vortex_body_materialuniqueid: int
    vortex_body_normalangularaxisfriction: int
    vortex_body_normalangularaxisfrictionmodel: int
    vortex_body_normalangularaxisslide: int
    vortex_body_normalangularaxisslip: int
    vortex_body_normalangularaxisstaticfrictionscale: int
    vortex_body_normalmangulararaxisfrictionmodel: int
    vortex_body_normangaxissameasprimangaxis: int
    vortex_body_primangulararaxisfrictionmodel: int
    vortex_body_primangularaxisfriction: int
    vortex_body_primangularaxisslide: int
    vortex_body_primangularaxisslip: int
    vortex_body_primangularaxisstaticfrictionscale: int
    vortex_body_primaxisvectorx: int
    vortex_body_primaxisvectory: int
    vortex_body_primaxisvectorz: int
    vortex_body_primlinearaxisfriction: int
    vortex_body_primlinearaxisfrictionmodel: int
    vortex_body_primlinearaxisslide: int
    vortex_body_primlinearaxisslip: int
    vortex_body_primlinearaxisstaticfrictionscale: int
    vortex_body_pureshapesasconvex: int
    vortex_body_randomshapesasterrain: int
    vortex_body_restitution: int
    vortex_body_restitutionthreshold: int
    vortex_body_secangaxissameasprimangaxis: int
    vortex_body_secangularaxisfriction: int
    vortex_body_secangularaxisfrictionmodel: int
    vortex_body_secangularaxisslide: int
    vortex_body_secangularaxisslip: int
    vortex_body_secangularaxisstaticfrictionscale: int
    vortex_body_seclinaxissameasprimlinaxis: int
    vortex_body_seclinearaxisfriction: int
    vortex_body_seclinearaxisfrictionmodel: int
    vortex_body_seclinearaxisslide: int
    vortex_body_seclinearaxisslip: int
    vortex_body_seclinearaxisstaticfrictionscale: int
    vortex_body_secmangulararaxisfrictionmodel: int
    vortex_body_skinthickness: int
    vortex_bodyfrictionmodel_box: int
    vortex_bodyfrictionmodel_neutral: int
    vortex_bodyfrictionmodel_none: int
    vortex_bodyfrictionmodel_prophigh: int
    vortex_bodyfrictionmodel_proplow: int
    vortex_bodyfrictionmodel_scaledbox: int
    vortex_bodyfrictionmodel_scaledboxfast: int
    vortex_global_autosleep: int
    vortex_global_bitcoded: int
    vortex_global_computeinertias: int
    vortex_global_constraintangularcompliance: int
    vortex_global_constraintangulardamping: int
    vortex_global_constraintangularkineticloss: int
    vortex_global_constraintlinearcompliance: int
    vortex_global_constraintlineardamping: int
    vortex_global_constraintlinearkineticloss: int
    vortex_global_contacttolerance: int
    vortex_global_internalscalingfactor: int
    vortex_global_multithreading: int
    vortex_global_stepsize: int
    vortex_joint_a0damping: int
    vortex_joint_a0frictioncoeff: int
    vortex_joint_a0frictionloss: int
    vortex_joint_a0frictionmaxforce: int
    vortex_joint_a0loss: int
    vortex_joint_a0stiffness: int
    vortex_joint_a1damping: int
    vortex_joint_a1frictioncoeff: int
    vortex_joint_a1frictionloss: int
    vortex_joint_a1frictionmaxforce: int
    vortex_joint_a1loss: int
    vortex_joint_a1stiffness: int
    vortex_joint_a2damping: int
    vortex_joint_a2frictioncoeff: int
    vortex_joint_a2frictionloss: int
    vortex_joint_a2frictionmaxforce: int
    vortex_joint_a2loss: int
    vortex_joint_a2stiffness: int
    vortex_joint_bitcoded: int
    vortex_joint_dependencyfactor: int
    vortex_joint_dependencyoffset: int
    vortex_joint_dependentobjectid: int
    vortex_joint_frictionenabledbc: int
    vortex_joint_frictionproportionalbc: int
    vortex_joint_lowerlimitdamping: int
    vortex_joint_lowerlimitmaxforce: int
    vortex_joint_lowerlimitrestitution: int
    vortex_joint_lowerlimitstiffness: int
    vortex_joint_motorconstraintfrictioncoeff: int
    vortex_joint_motorconstraintfrictionloss: int
    vortex_joint_motorconstraintfrictionmaxforce: int
    vortex_joint_motorfrictionenabled: int
    vortex_joint_objectid: int
    vortex_joint_p0damping: int
    vortex_joint_p0frictioncoeff: int
    vortex_joint_p0frictionloss: int
    vortex_joint_p0frictionmaxforce: int
    vortex_joint_p0loss: int
    vortex_joint_p0stiffness: int
    vortex_joint_p1damping: int
    vortex_joint_p1frictioncoeff: int
    vortex_joint_p1frictionloss: int
    vortex_joint_p1frictionmaxforce: int
    vortex_joint_p1loss: int
    vortex_joint_p1stiffness: int
    vortex_joint_p2damping: int
    vortex_joint_p2frictioncoeff: int
    vortex_joint_p2frictionloss: int
    vortex_joint_p2frictionmaxforce: int
    vortex_joint_p2loss: int
    vortex_joint_p2stiffness: int
    vortex_joint_pospid1: int
    vortex_joint_pospid2: int
    vortex_joint_pospid3: int
    vortex_joint_proportionalmotorfriction: int
    vortex_joint_relaxationenabledbc: int
    vortex_joint_upperlimitdamping: int
    vortex_joint_upperlimitmaxforce: int
    vortex_joint_upperlimitrestitution: int
    vortex_joint_upperlimitstiffness: int

    # --- Functions ---
    def Object(self, handle: int) -> dict:
        """map object = sim.Object(int handle)"""
        ...

    def acquireLock(self) -> None:
        """sim.acquireLock()"""
        ...

    def addDrawingObject(self, objectType: int, size: float, duplicateTolerance: float, parentObjectHandle: int, maxItemCount: int, color: Any = nil) -> int:
        """int drawingObjectHandle = sim.addDrawingObject(int objectType, float size, float duplicateTolerance, int parentObjectHandle, int maxItemCount, float[3] color=nil)"""
        ...

    def addDrawingObjectItem(self, drawingObjectHandle: int, itemData: list) -> int:
        """int result = sim.addDrawingObjectItem(int drawingObjectHandle, float[] itemData)"""
        ...

    def addForce(self, shapeHandle: int, position: Any, force: Any) -> None:
        """sim.addForce(int shapeHandle, float[3] position, float[3] force)"""
        ...

    def addForceAndTorque(self) -> Tuple[Any, Any]:
        """sim.addForceAndTorque(int shapeHandle, float[3] force=nil, float[3] torque=nil)"""
        ...

    def addGraphCurve(self, graphHandle: int, curveName: str, dim: int, streamIds: Any, defaultValues: Any, unitStr: str, options: int = 0, color: Any = ..., arg8: Any, arg9: Any, curveWidth: int = 2) -> int:
        """int curveId = sim.addGraphCurve(int graphHandle, string curveName, int dim, int[2..3] streamIds, float[2..3] defaultValues, string unitStr, int options=0, float[3] color={1, 1, 0}, int curveWidth=2)"""
        ...

    def addGraphStream(self, graphHandle: int, streamName: str, unit: str, options: int = 0, color: Any = ..., arg5: Any, arg6: Any, cyclicRange: float = pi) -> int:
        """int streamId = sim.addGraphStream(int graphHandle, string streamName, string unit, int options=0, float[3] color={1, 0, 0}, float cyclicRange=pi)"""
        ...

    def addItemToCollection(self, collectionHandle: int, what: int, objectHandle: int, options: int) -> None:
        """sim.addItemToCollection(int collectionHandle, int what, int objectHandle, int options)"""
        ...

    def addLog(self, verbosityLevel: int, logMessage: str) -> None:
        """sim.addLog(int verbosityLevel, string logMessage)"""
        ...

    def addParticleObject(self, objectType: int, size: float, density: float, params: list, lifeTime: float, maxItemCount: int, color: Any = nil) -> int:
        """int particleObjectHandle = sim.addParticleObject(int objectType, float size, float density, float[] params, float lifeTime, int maxItemCount, float[3] color=nil)"""
        ...

    def addParticleObjectItem(self, objectHandle: int, itemData: list) -> None:
        """sim.addParticleObjectItem(int objectHandle, float[] itemData)"""
        ...

    def addReferencedHandle(self) -> Tuple[Any, int, str]:
        """sim.addReferencedHandle(int objectHandle, int referencedHandle, string tag='', map opts={})"""
        ...

    def adjustView(self, viewHandleOrIndex: int, objectHandle: int, options: int, viewLabel: str = nil) -> int:
        """int res = sim.adjustView(int viewHandleOrIndex, int objectHandle, int options, string viewLabel=nil)"""
        ...

    def alignShapeBB(self, shapeHandle: int, pose: Any) -> int:
        """int result = sim.alignShapeBB(int shapeHandle, float[7] pose)"""
        ...

    def alphaBetaGammaToYawPitchRoll(self, alphaAngle: float, betaAngle: float, gammaAngle: float) -> Tuple[float, float, float]:
        """float yawAngle, float pitchAngle, float rollAngle = sim.alphaBetaGammaToYawPitchRoll(float alphaAngle, float betaAngle, float gammaAngle)"""
        ...

    def announceSceneContentChange(self) -> int:
        """int result = sim.announceSceneContentChange()"""
        ...

    def auxiliaryConsoleClose(self, consoleHandle: int) -> int:
        """int result = sim.auxiliaryConsoleClose(int consoleHandle)"""
        ...

    def auxiliaryConsoleOpen(self, title: str, maxLines: int, mode: int, position: Any = nil, size: Any = nil, textColor: Any = nil, backgroundColor: Any = nil) -> int:
        """int consoleHandle = sim.auxiliaryConsoleOpen(string title, int maxLines, int mode, int[2] position=nil, int[2] size=nil, float[3] textColor=nil, float[3] backgroundColor=nil)"""
        ...

    def auxiliaryConsolePrint(self, consoleHandle: int, text: str) -> int:
        """int result = sim.auxiliaryConsolePrint(int consoleHandle, string text)"""
        ...

    def auxiliaryConsoleShow(self, consoleHandle: int, showState: bool) -> int:
        """int result = sim.auxiliaryConsoleShow(int consoleHandle, bool showState)"""
        ...

    def broadcastMsg(self) -> Tuple[Any, int]:
        """sim.broadcastMsg(map message, int options=0)"""
        ...

    def buildIdentityMatrix(self) -> Any:
        """float[12] matrix = sim.buildIdentityMatrix()"""
        ...

    def buildMatrix(self, position: Any, eulerAngles: Any) -> Any:
        """float[12] matrix = sim.buildMatrix(float[3] position, float[3] eulerAngles)"""
        ...

    def buildPose(self, position: Any, eulerAnglesOrAxis: Any, mode: int = 0, axis2: Any = nil) -> Any:
        """float[7] pose = sim.buildPose(float[3] position, float[3] eulerAnglesOrAxis, int mode=0, float[3] axis2=nil)"""
        ...

    def callScriptFunction(self, functionName: str, scriptHandle: int, *args) -> Any:
        """... = sim.callScriptFunction(string functionName, int scriptHandle, ...)"""
        ...

    def cameraFitToView(self, viewHandleOrIndex: int, objectHandles: list = nil, options: int = 0, scaling: float = 1.0) -> int:
        """int result = sim.cameraFitToView(int viewHandleOrIndex, int[] objectHandles=nil, int options=0, float scaling=1.0)"""
        ...

    def cancelScheduledExecution(self, id: int) -> bool:
        """bool canceled = sim.cancelScheduledExecution(int id)"""
        ...

    def changeEntityColor(self, entityHandle: int, newColor: Any, colorComponent: int = sim.colorcomponent_ambient_diffuse) -> list:
        """map[] originalColorData = sim.changeEntityColor(int entityHandle, float[3] newColor, int colorComponent=sim.colorcomponent_ambient_diffuse)"""
        ...

    def checkCollision(self, entity1Handle: int, entity2Handle: int) -> Tuple[int, Any]:
        """int result, int[2] collidingObjects = sim.checkCollision(int entity1Handle, int entity2Handle)"""
        ...

    def checkCollisionEx(self, entity1Handle: int, entity2Handle: int) -> Tuple[int, list]:
        """int segmentCount, float[6..*] segmentData = sim.checkCollisionEx(int entity1Handle, int entity2Handle)"""
        ...

    def checkDistance(self, entity1Handle: int, entity2Handle: int, threshold: float = 0.0) -> Tuple[int, Any, Any]:
        """int result, float[7] distanceData, int[2] objectHandlePair = sim.checkDistance(int entity1Handle, int entity2Handle, float threshold=0.0)"""
        ...

    def checkOctreePointOccupancy(self, octreeHandle: int, options: int, points: list) -> Tuple[int, int, int, int]:
        """int result, int tag, int locationLow, int locationHigh = sim.checkOctreePointOccupancy(int octreeHandle, int options, float[] points)"""
        ...

    def checkProximitySensor(self, sensorHandle: int, entityHandle: int) -> Tuple[int, float, Any, int, Any]:
        """int result, float distance, float[3] detectedPoint, int detectedObjectHandle, float[3] normalVector = sim.checkProximitySensor(int sensorHandle, int entityHandle)"""
        ...

    def checkProximitySensorEx(self, sensorHandle: int, entityHandle: int, mode: int, threshold: float, maxAngle: float) -> Tuple[int, float, Any, int, Any]:
        """int result, float distance, float[3] detectedPoint, int detectedObjectHandle, float[3] normalVector = sim.checkProximitySensorEx(int sensorHandle, int entityHandle, int mode, float threshold, float maxAngle)"""
        ...

    def checkProximitySensorEx2(self, sensorHandle: int, vertices: list, itemType: int, itemCount: int, mode: int, threshold: float, maxAngle: float) -> Tuple[int, float, Any, Any]:
        """int result, float distance, float[3] detectedPoint, float[3] normalVector = sim.checkProximitySensorEx2(int sensorHandle, float[3..*] vertices, int itemType, int itemCount, int mode, float threshold, float maxAngle)"""
        ...

    def checkVisionSensor(self, sensorHandle: int, entityHandle: int) -> Tuple[int, list, list]:
        """int result, float[] auxPacket1, float[] auxPacket2 = sim.checkVisionSensor(int sensorHandle, int entityHandle)"""
        ...

    def checkVisionSensorEx(self, sensorHandle: int, entityHandle: int, returnImage: bool) -> list:
        """float[] theBuffer = sim.checkVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)"""
        ...

    def clearBufferSignal(self, signalName: str) -> None:
        """sim.clearBufferSignal(string signalName)"""
        ...

    def clearFloatSignal(self, signalName: str) -> None:
        """sim.clearFloatSignal(string signalName)"""
        ...

    def clearInt32Signal(self, signalName: str) -> None:
        """sim.clearInt32Signal(string signalName)"""
        ...

    def clearStringSignal(self, signalName: str) -> None:
        """sim.clearStringSignal(string signalName)"""
        ...

    def closeScene(self) -> int:
        """int result = sim.closeScene()"""
        ...

    def combineRgbImages(self, img1: bytes, img1Res: Any, img2: bytes, img2Res: Any, operation: int) -> bytes:
        """buffer outImg = sim.combineRgbImages(buffer img1, int[2] img1Res, buffer img2, int[2] img2Res, int operation)"""
        ...

    def computeMassAndInertia(self, shapeHandle: int, density: float) -> int:
        """int result = sim.computeMassAndInertia(int shapeHandle, float density)"""
        ...

    def convertPropertyValue(self, value: Any, fromType: int, toType: int) -> Any:
        """any value = sim.convertPropertyValue(any value, int fromType, int toType)"""
        ...

    def copyPasteObjects(self, objectHandles: list, options: int = 0) -> list:
        """int[1..*] copiedObjectHandles = sim.copyPasteObjects(int[1..*] objectHandles, int options=0)"""
        ...

    def copyTable(self, original: list) -> list:
        """any[] copy = sim.copyTable(any[] original)"""
        ...

    def createCollection(self, options: int = 0) -> int:
        """int collectionHandle = sim.createCollection(int options=0)"""
        ...

    def createDummy(self, size: float) -> int:
        """int dummyHandle = sim.createDummy(float size)"""
        ...

    def createForceSensor(self, options: int, intParams: Any, floatParams: Any) -> int:
        """int sensorHandle = sim.createForceSensor(int options, int[5] intParams, float[5] floatParams)"""
        ...

    def createHeightfieldShape(self, options: int, shadingAngle: float, xPointCount: int, yPointCount: int, xSize: float, heights: list) -> int:
        """int shapeHandle = sim.createHeightfieldShape(int options, float shadingAngle, int xPointCount, int yPointCount, float xSize, float[] heights)"""
        ...

    def createJoint(self, jointType: int, jointMode: int, options: int, sizes: Any = nil) -> int:
        """int jointHandle = sim.createJoint(int jointType, int jointMode, int options, float[2] sizes=nil)"""
        ...

    def createOctree(self, voxelSize: float, options: int, pointSize: float) -> int:
        """int handle = sim.createOctree(float voxelSize, int options, float pointSize)"""
        ...

    def createPath(self, ctrlPts: list, options: int = 0, subdiv: int = 100, smoothness: float = 1.0, orientationMode: int = 0, upVector: Any = ..., arg6: Any, arg7: Any) -> int:
        """int pathHandle = sim.createPath(float[] ctrlPts, int options=0, int subdiv=100, float smoothness=1.0, int orientationMode=0, float[3] upVector={0, 0, 1})"""
        ...

    def createPointCloud(self, maxVoxelSize: float, maxPtCntPerVoxel: int, options: int, pointSize: float) -> int:
        """int handle = sim.createPointCloud(float maxVoxelSize, int maxPtCntPerVoxel, int options, float pointSize)"""
        ...

    def createPrimitiveShape(self, primitiveType: int, sizes: Any, options: int = 0) -> int:
        """int shapeHandle = sim.createPrimitiveShape(int primitiveType, float[3] sizes, int options=0)"""
        ...

    def createProximitySensor(self, sensorType: int, subType: int, options: int, intParams: Any, floatParams: Any) -> int:
        """int sensorHandle = sim.createProximitySensor(int sensorType, int subType, int options, int[8] intParams, float[15] floatParams)"""
        ...

    def createScript(self, scriptType: int, scriptString: str, options: int = 0, lang: str = '') -> int:
        """int scriptHandle = sim.createScript(int scriptType, string scriptString, int options=0, string lang='')"""
        ...

    def createShape(self, options: int, shadingAngle: float, vertices: list, indices: list, normals: list, textureCoordinates: list, texture: bytes, textureResolution: Any) -> int:
        """int shapeHandle = sim.createShape(int options, float shadingAngle, float[] vertices, int[] indices, float[] normals, float[] textureCoordinates, buffer texture, int[2] textureResolution)"""
        ...

    def createTexture(self, fileName: str, options: int, planeSizes: Any = nil, scalingUV: Any = nil, xy_g: Any = nil, fixedResolution: int = 0, resolution: Any = nil) -> Tuple[int, int, Any]:
        """int shapeHandle, int textureId, int[2] resolution = sim.createTexture(string fileName, int options, float[2] planeSizes=nil, float[2] scalingUV=nil, float[2] xy_g=nil, int fixedResolution=0, int[2] resolution=nil)"""
        ...

    def createVisionSensor(self, options: int, intParams: Any, floatParams: Any) -> int:
        """int sensorHandle = sim.createVisionSensor(int options, int[4] intParams, float[11] floatParams)"""
        ...

    def destroyCollection(self, collectionHandle: int) -> None:
        """sim.destroyCollection(int collectionHandle)"""
        ...

    def destroyGraphCurve(self, graphHandle: int, curveId: int) -> None:
        """sim.destroyGraphCurve(int graphHandle, int curveId)"""
        ...

    def duplicateGraphCurveToStatic(self, graphHandle: int, curveId: int, curveName: str = '') -> int:
        """int curveId = sim.duplicateGraphCurveToStatic(int graphHandle, int curveId, string curveName='')"""
        ...

    def executeLuaCode(self, theCode: str) -> Tuple[bool, Any]:
        """bool success, any value = sim.executeLuaCode(string theCode)"""
        ...

    def executeScriptString(self, stringToExecute: str, scriptHandle: int) -> Tuple[int, Any]:
        """int result, any value = sim.executeScriptString(string stringToExecute, int scriptHandle)"""
        ...

    def exportMesh(self, fileformat: int, pathAndFilename: str, options: int, scalingFactor: float, vertices: list, indices: list) -> None:
        """sim.exportMesh(int fileformat, string pathAndFilename, int options, float scalingFactor, float[1..*] vertices, int[1..*] indices)"""
        ...

    def fastIdleLoop(self, enable: bool) -> None:
        """sim.fastIdleLoop(bool enable)"""
        ...

    def floatingViewAdd(self, posX: float, posY: float, sizeX: float, sizeY: float, options: int) -> int:
        """int floatingViewHandle = sim.floatingViewAdd(float posX, float posY, float sizeX, float sizeY, int options)"""
        ...

    def floatingViewRemove(self, floatingViewHandle: int) -> int:
        """int result = sim.floatingViewRemove(int floatingViewHandle)"""
        ...

    def generateShapeFromPath(self, path: list, section: list, options: int = 0, upVector: Any = ..., arg4: Any, arg5: Any) -> int:
        """int shapeHandle = sim.generateShapeFromPath(float[] path, float[] section, int options=0, float[3] upVector={0.0, 0.0, 1.0})"""
        ...

    def generateTextShape(self, txt: str, color: Any = ..., arg2: Any, arg3: Any, height: float = 0.1, centered: bool = false, alphabetLocation: str = nil) -> int:
        """int modelHandle = sim.generateTextShape(string txt, float[3] color={1, 1, 1}, float height=0.1, bool centered=false, string alphabetLocation=nil)"""
        ...

    def generateTimeOptimalTrajectory(self, path: list, pathLengths: list, minMaxVel: list, minMaxAccel: list, trajPtSamples: int = 1000, boundaryCondition: str = 'not-a-knot', timeout: float = 5) -> Tuple[list, list]:
        """float[] path, float[] times = sim.generateTimeOptimalTrajectory(float[] path, float[] pathLengths, float[] minMaxVel, float[] minMaxAccel, int trajPtSamples=1000, string boundaryCondition='not-a-knot', float timeout=5)"""
        ...

    def getAlternateConfigs(self, jointHandles: list, inputConfig: list, tipHandle: int = -1, lowLimits: list = nil, ranges: list = nil) -> list:
        """float[] configs = sim.getAlternateConfigs(int[] jointHandles, float[] inputConfig, int tipHandle=-1, float[] lowLimits=nil, float[] ranges=nil)"""
        ...

    def getApiFunc(self, scriptHandle: int, apiWord: str) -> list:
        """string[] funcsAndVars = sim.getApiFunc(int scriptHandle, string apiWord)"""
        ...

    def getApiInfo(self, scriptHandle: int, apiWord: str) -> str:
        """string info = sim.getApiInfo(int scriptHandle, string apiWord)"""
        ...

    def getArrayParam(self, parameter: int) -> Any:
        """float[3] arrayOfValues = sim.getArrayParam(int parameter)"""
        ...

    def getAutoYieldDelay(self) -> float:
        """float dt = sim.getAutoYieldDelay()"""
        ...

    def getBoolParam(self, parameter: int) -> bool:
        """bool boolState = sim.getBoolParam(int parameter)"""
        ...

    def getBoolProperty(self, target: int, pName: str, options: dict = ...) -> bool:
        """bool pValue = sim.getBoolProperty(int target, string pName, map options={})"""
        ...

    def getBufferProperty(self, target: int, pName: str, options: dict = ...) -> bytes:
        """buffer pValue = sim.getBufferProperty(int target, string pName, map options={})"""
        ...

    def getBufferSignal(self, signalName: str) -> bytes:
        """buffer signalValue = sim.getBufferSignal(string signalName)"""
        ...

    def getClosestPosOnPath(self, path: list, pathLengths: list, absPt: Any) -> float:
        """float posAlongPath = sim.getClosestPosOnPath(float[] path, float[] pathLengths, float[3] absPt)"""
        ...

    def getCollectionObjects(self, collectionHandle: int) -> list:
        """int[] objectHandles = sim.getCollectionObjects(int collectionHandle)"""
        ...

    def getColorProperty(self, target: int, pName: str, options: dict = ...) -> Any:
        """float[3] pValue = sim.getColorProperty(int target, string pName, map options={})"""
        ...

    def getConfigDistance(self, configA: list, configB: list, metric: list = nil, types: list = nil) -> float:
        """float distance = sim.getConfigDistance(float[] configA, float[] configB, float[] metric=nil, int[] types=nil)"""
        ...

    def getContactInfo(self, dynamicPass: int, objectHandle: int, index: int) -> Tuple[Any, Any, Any, Any]:
        """int[2] collidingObjects, float[3] collisionPoint, float[3] reactionForce, float[3] normalVector = sim.getContactInfo(int dynamicPass, int objectHandle, int index)"""
        ...

    def getEngineBoolParam(self, paramId: int, objectHandle: int) -> bool:
        """bool boolParam = sim.getEngineBoolParam(int paramId, int objectHandle)"""
        ...

    def getEngineFloatParam(self, paramId: int, objectHandle: int) -> float:
        """float floatParam = sim.getEngineFloatParam(int paramId, int objectHandle)"""
        ...

    def getEngineInt32Param(self, paramId: int, objectHandle: int) -> int:
        """int int32Param = sim.getEngineInt32Param(int paramId, int objectHandle)"""
        ...

    def getEulerAnglesFromMatrix(self, matrix: Any) -> Any:
        """float[3] eulerAngles = sim.getEulerAnglesFromMatrix(float[12] matrix)"""
        ...

    def getExplicitHandling(self, objectHandle: int) -> int:
        """int explicitHandlingFlags = sim.getExplicitHandling(int objectHandle)"""
        ...

    def getExtensionString(self, objectHandle: int, index: int, key: str = nil) -> str:
        """string theString = sim.getExtensionString(int objectHandle, int index, string key=nil)"""
        ...

    def getFloatArrayProperty(self, target: int, pName: str, options: dict = ...) -> list:
        """float[] pValue = sim.getFloatArrayProperty(int target, string pName, map options={})"""
        ...

    def getFloatParam(self, parameter: int) -> float:
        """float floatState = sim.getFloatParam(int parameter)"""
        ...

    def getFloatProperty(self, target: int, pName: str, options: dict = ...) -> float:
        """float pValue = sim.getFloatProperty(int target, string pName, map options={})"""
        ...

    def getFloatSignal(self, signalName: str) -> float:
        """float signalValue = sim.getFloatSignal(string signalName)"""
        ...

    def getGenesisEvents(self) -> list:
        """map[] events = sim.getGenesisEvents()"""
        ...

    def getGraphCurve(self, graphHandle: int, graphType: int, curveIndex: int) -> Tuple[str, int, Any, list, list, Any, int, int]:
        """string label, int attributes, float[3] curveColor, float[] xData, float[] yData, float[6] minMax, int curveId, int curveWidth = sim.getGraphCurve(int graphHandle, int graphType, int curveIndex)"""
        ...

    def getGraphInfo(self, graphHandle: int) -> Tuple[int, Any, Any]:
        """int bitCoded, float[3] bgColor, float[3] fgColor = sim.getGraphInfo(int graphHandle)"""
        ...

    def getInt32Param(self, parameter: int) -> int:
        """int intState = sim.getInt32Param(int parameter)"""
        ...

    def getInt32Signal(self, signalName: str) -> int:
        """int signalValue = sim.getInt32Signal(string signalName)"""
        ...

    def getIntArray2Property(self, target: int, pName: str, options: dict = ...) -> Any:
        """int[2] pValue = sim.getIntArray2Property(int target, string pName, map options={})"""
        ...

    def getIntArrayProperty(self, target: int, pName: str, options: dict = ...) -> list:
        """int[] pValue = sim.getIntArrayProperty(int target, string pName, map options={})"""
        ...

    def getIntProperty(self, target: int, pName: str, options: dict = ...) -> int:
        """int pValue = sim.getIntProperty(int target, string pName, map options={})"""
        ...

    def getIsRealTimeSimulation(self) -> int:
        """int result = sim.getIsRealTimeSimulation()"""
        ...

    def getJointDependency(self, jointHandle: int) -> Tuple[int, float, float]:
        """int masterJointHandle, float offset, float multCoeff = sim.getJointDependency(int jointHandle)"""
        ...

    def getJointForce(self, jointHandle: int) -> float:
        """float forceOrTorque = sim.getJointForce(int jointHandle)"""
        ...

    def getJointInterval(self, objectHandle: int) -> Tuple[bool, Any]:
        """bool cyclic, float[2] interval = sim.getJointInterval(int objectHandle)"""
        ...

    def getJointMode(self, jointHandle: int) -> Tuple[int, int]:
        """int jointMode, int options = sim.getJointMode(int jointHandle)"""
        ...

    def getJointPosition(self, objectHandle: int) -> float:
        """float position = sim.getJointPosition(int objectHandle)"""
        ...

    def getJointTargetForce(self, jointHandle: int) -> float:
        """float forceOrTorque = sim.getJointTargetForce(int jointHandle)"""
        ...

    def getJointTargetPosition(self, objectHandle: int) -> float:
        """float targetPosition = sim.getJointTargetPosition(int objectHandle)"""
        ...

    def getJointTargetVelocity(self, objectHandle: int) -> float:
        """float targetVelocity = sim.getJointTargetVelocity(int objectHandle)"""
        ...

    def getJointType(self, objectHandle: int) -> int:
        """int jointType = sim.getJointType(int objectHandle)"""
        ...

    def getJointVelocity(self, jointHandle: int) -> float:
        """float velocity = sim.getJointVelocity(int jointHandle)"""
        ...

    def getLastInfo(self) -> str:
        """string info = sim.getLastInfo()"""
        ...

    def getLightParameters(self, lightHandle: int) -> Tuple[int, Any, Any, Any]:
        """int state, float[3] zero, float[3] diffusePart, float[3] specular = sim.getLightParameters(int lightHandle)"""
        ...

    def getLinkDummy(self, dummyHandle: int) -> int:
        """int linkDummyHandle = sim.getLinkDummy(int dummyHandle)"""
        ...

    def getLoadedPlugins(self) -> list:
        """string[] names = sim.getLoadedPlugins()"""
        ...

    def getLongProperty(self, target: int, pName: str, options: dict = ...) -> int:
        """int pValue = sim.getLongProperty(int target, string pName, map options={})"""
        ...

    def getMatchingPersistentDataTags(self, pattern: str) -> list:
        """string[] tags = sim.getMatchingPersistentDataTags(string pattern)"""
        ...

    def getMatrixInverse(self, matrix: Any) -> Any:
        """float[12] matrix = sim.getMatrixInverse(float[12] matrix)"""
        ...

    def getModelBB(self, handle: int) -> Any:
        """float[3] size = sim.getModelBB(int handle)"""
        ...

    def getModelProperty(self, objectHandle: int) -> int:
        """int property = sim.getModelProperty(int objectHandle)"""
        ...

    def getNamedBoolParam(self, name: str) -> bool:
        """bool value = sim.getNamedBoolParam(string name)"""
        ...

    def getNamedFloatParam(self, name: str) -> float:
        """float value = sim.getNamedFloatParam(string name)"""
        ...

    def getNamedInt32Param(self, name: str) -> int:
        """int value = sim.getNamedInt32Param(string name)"""
        ...

    def getNamedStringParam(self, paramName: str) -> bytes:
        """buffer stringParam = sim.getNamedStringParam(string paramName)"""
        ...

    def getNavigationMode(self) -> int:
        """int navigationMode = sim.getNavigationMode()"""
        ...

    def getObject(self, path: str, options: dict = ...) -> int:
        """int objectHandle = sim.getObject(string path, map options={})"""
        ...

    def getObjectAlias(self, objectHandle: int, options: int = -1) -> str:
        """string objectAlias = sim.getObjectAlias(int objectHandle, int options=-1)"""
        ...

    def getObjectAliasRelative(self, handle: int, baseHandle: int, options: int = -1) -> str:
        """string alias = sim.getObjectAliasRelative(int handle, int baseHandle, int options=-1)"""
        ...

    def getObjectChild(self, objectHandle: int, index: int) -> int:
        """int childObjectHandle = sim.getObjectChild(int objectHandle, int index)"""
        ...

    def getObjectChildPose(self, objectHandle: int) -> Any:
        """float[7] pose = sim.getObjectChildPose(int objectHandle)"""
        ...

    def getObjectColor(self, objectHandle: int, index: int, colorComponent: int) -> Any:
        """float[3] rgbData = sim.getObjectColor(int objectHandle, int index, int colorComponent)"""
        ...

    def getObjectFloatArrayParam(self, objectHandle: int, parameterID: int) -> list:
        """float[] params = sim.getObjectFloatArrayParam(int objectHandle, int parameterID)"""
        ...

    def getObjectFloatParam(self, objectHandle: int, parameterID: int) -> float:
        """float parameter = sim.getObjectFloatParam(int objectHandle, int parameterID)"""
        ...

    def getObjectFromUid(self) -> Tuple[Any, dict]:
        """sim.getObjectFromUid(int uid, map options={})"""
        ...

    def getObjectHandle(self, path: str, options: dict = ...) -> int:
        """int handle = sim.getObjectHandle(string path, map options={})"""
        ...

    def getObjectHierarchyOrder(self, objectHandle: int) -> Tuple[int, int]:
        """int order, int totalSiblingsCount = sim.getObjectHierarchyOrder(int objectHandle)"""
        ...

    def getObjectInt32Param(self, objectHandle: int, parameterID: int) -> int:
        """int parameter = sim.getObjectInt32Param(int objectHandle, int parameterID)"""
        ...

    def getObjectMatrix(self, objectHandle: int, relativeToObjectHandle: int = sim.handle_world) -> Any:
        """float[12] matrix = sim.getObjectMatrix(int objectHandle, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def getObjectOrientation(self, objectHandle: int, relativeToObjectHandle: int = sim.handle_world) -> Any:
        """float[3] eulerAngles = sim.getObjectOrientation(int objectHandle, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def getObjectParent(self, objectHandle: int) -> int:
        """int parentObjectHandle = sim.getObjectParent(int objectHandle)"""
        ...

    def getObjectPose(self, objectHandle: int, relativeToObjectHandle: int = sim.handle_world) -> Any:
        """float[7] pose = sim.getObjectPose(int objectHandle, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def getObjectPosition(self, objectHandle: int, relativeToObjectHandle: int = sim.handle_world) -> Any:
        """float[3] position = sim.getObjectPosition(int objectHandle, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def getObjectProperty(self, objectHandle: int) -> int:
        """int property = sim.getObjectProperty(int objectHandle)"""
        ...

    def getObjectQuaternion(self, objectHandle: int, relativeToObjectHandle: int = sim.handle_world) -> Any:
        """float[4] quaternion = sim.getObjectQuaternion(int objectHandle, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def getObjectSel(self) -> list:
        """int[] objectHandles = sim.getObjectSel()"""
        ...

    def getObjectSizeFactor(self, ObjectHandle: int) -> float:
        """float sizeFactor = sim.getObjectSizeFactor(int ObjectHandle)"""
        ...

    def getObjectSpecialProperty(self, objectHandle: int) -> int:
        """int property = sim.getObjectSpecialProperty(int objectHandle)"""
        ...

    def getObjectStringParam(self, objectHandle: int, parameterID: int) -> bytes:
        """buffer parameter = sim.getObjectStringParam(int objectHandle, int parameterID)"""
        ...

    def getObjectType(self, objectHandle: int) -> int:
        """int objectType = sim.getObjectType(int objectHandle)"""
        ...

    def getObjectUid(self, objectHandle: int) -> int:
        """int uid = sim.getObjectUid(int objectHandle)"""
        ...

    def getObjectVelocity(self, objectHandle: int) -> Tuple[Any, Any]:
        """float[3] linearVelocity, float[3] angularVelocity = sim.getObjectVelocity(int objectHandle)"""
        ...

    def getObjects(self, index: int, objectType: int) -> int:
        """int objectHandle = sim.getObjects(int index, int objectType)"""
        ...

    def getObjectsInTree(self, treeBaseHandle: int, objectType: int = sim.handle_all, options: int = 0) -> list:
        """int[] objects = sim.getObjectsInTree(int treeBaseHandle, int objectType=sim.handle_all, int options=0)"""
        ...

    def getObjectsWithTag(self, tagName: str, justModels: bool = false) -> list:
        """int[] objs = sim.getObjectsWithTag(string tagName, bool justModels=false)"""
        ...

    def getOctreeVoxels(self, octreeHandle: int) -> list:
        """float[] voxels = sim.getOctreeVoxels(int octreeHandle)"""
        ...

    def getPage(self) -> int:
        """int pageIndex = sim.getPage()"""
        ...

    # Could not generate stub for: sim.getPathInterpolatedConfig
    # Original signature: float[] config = sim.getPathInterpolatedConfig(float[] path, float[] pathLengths, float t, map method={type='linear', strength=1.0, forceOpen=false}, int[] types=nil)

    def getPathLengths(self, path: list, dof: int, distCallback: Any = nil) -> Tuple[list, float]:
        """float[] pathLengths, float totalLength = sim.getPathLengths(float[] path, int dof, func distCallback=nil)"""
        ...

    def getPluginInfo(self, pluginName: str, infoType: int) -> str:
        """string info = sim.getPluginInfo(string pluginName, int infoType)"""
        ...

    def getPluginName(self, index: int) -> str:
        """string pluginName = sim.getPluginName(int index)"""
        ...

    def getPointCloudOptions(self, pointCloudHandle: int) -> Tuple[float, int, int, float]:
        """float maxVoxelSize, int maxPtCntPerVoxel, int options, float pointSize = sim.getPointCloudOptions(int pointCloudHandle)"""
        ...

    def getPointCloudPoints(self, pointCloudHandle: int) -> list:
        """float[] points = sim.getPointCloudPoints(int pointCloudHandle)"""
        ...

    def getPoseInverse(self, pose: Any) -> Any:
        """float[7] pose = sim.getPoseInverse(float[7] pose)"""
        ...

    def getPoseProperty(self, target: int, pName: str, options: dict = ...) -> Any:
        """float[7] pValue = sim.getPoseProperty(int target, string pName, map options={})"""
        ...

    def getProperties(self, target: int, opts: dict = ...) -> dict:
        """map values = sim.getProperties(int target, map opts={})"""
        ...

    def getPropertiesInfos(self, target: int, opts: dict = ...) -> dict:
        """map infos = sim.getPropertiesInfos(int target, map opts={})"""
        ...

    def getProperty(self, target: int, pName: str, options: dict = ...) -> Any:
        """any pValue = sim.getProperty(int target, string pName, map options={})"""
        ...

    def getPropertyInfo(self, target: int, pName: str, options: dict = ...) -> Tuple[int, int, str]:
        """int pType, int pFlags, string description = sim.getPropertyInfo(int target, string pName, map options={})"""
        ...

    def getPropertyName(self, target: int, index: int, options: dict = ...) -> Tuple[str, str]:
        """string pName, string appartenance = sim.getPropertyName(int target, int index, map options={})"""
        ...

    def getPropertyTypeString(self, pType: int) -> str:
        """string pTypeStr = sim.getPropertyTypeString(int pType)"""
        ...

    def getQuaternionInverse(self, quat: Any) -> Any:
        """float[4] quat = sim.getQuaternionInverse(float[4] quat)"""
        ...

    def getQuaternionProperty(self, target: int, pName: str, options: dict = ...) -> Any:
        """float[4] pValue = sim.getQuaternionProperty(int target, string pName, map options={})"""
        ...

    def getRandom(self, seed: int = nil) -> float:
        """float randomNumber = sim.getRandom(int seed=nil)"""
        ...

    def getRealTimeSimulation(self) -> bool:
        """bool result = sim.getRealTimeSimulation()"""
        ...

    def getReferencedHandle(self, objectHandle: int, tag: str = '') -> int:
        """int referencedHandle = sim.getReferencedHandle(int objectHandle, string tag='')"""
        ...

    def getReferencedHandles(self, objectHandle: int, tag: str = '') -> list:
        """int[] referencedHandles = sim.getReferencedHandles(int objectHandle, string tag='')"""
        ...

    def getReferencedHandlesTags(self, objectHandle: int) -> list:
        """string[] tags = sim.getReferencedHandlesTags(int objectHandle)"""
        ...

    def getRotationAxis(self, matrixStart: Any, matrixGoal: Any) -> Tuple[Any, float]:
        """float[3] axis, float angle = sim.getRotationAxis(float[12] matrixStart, float[12] matrixGoal)"""
        ...

    def getScaledImage(self, imageIn: bytes, resolutionIn: Any, desiredResolutionOut: Any, options: int) -> Tuple[bytes, Any]:
        """buffer imageOut, int[2] effectiveResolutionOut = sim.getScaledImage(buffer imageIn, int[2] resolutionIn, int[2] desiredResolutionOut, int options)"""
        ...

    def getScript(self, scriptType: int, scriptName: str = '') -> int:
        """int scriptHandle = sim.getScript(int scriptType, string scriptName='')"""
        ...

    def getScriptFunctions(self, scriptHandle: int) -> dict:
        """map wrapper = sim.getScriptFunctions(int scriptHandle)"""
        ...

    def getSettingBool(self, key: str) -> bool:
        """bool value = sim.getSettingBool(string key)"""
        ...

    def getSettingFloat(self, key: str) -> float:
        """float value = sim.getSettingFloat(string key)"""
        ...

    def getSettingInt32(self, key: str) -> int:
        """int value = sim.getSettingInt32(string key)"""
        ...

    def getSettingString(self, key: str) -> str:
        """string value = sim.getSettingString(string key)"""
        ...

    def getShapeAppearance(self, handle: int, opts: dict = ...) -> dict:
        """map savedData = sim.getShapeAppearance(int handle, map opts={})"""
        ...

    def getShapeBB(self, shapeHandle: int) -> Tuple[Any, Any]:
        """float[3] size, float[7] pose = sim.getShapeBB(int shapeHandle)"""
        ...

    def getShapeColor(self, shapeHandle: int, colorName: str, colorComponent: int) -> Tuple[int, list]:
        """int result, float[] rgbData = sim.getShapeColor(int shapeHandle, string colorName, int colorComponent)"""
        ...

    def getShapeGeomInfo(self, shapeHandle: int) -> Tuple[int, int, Any]:
        """int result, int pureType, float[4] dimensions = sim.getShapeGeomInfo(int shapeHandle)"""
        ...

    def getShapeInertia(self, shapeHandle: int) -> Tuple[Any, Any]:
        """float[9] inertiaMatrix, float[12] comMatrix = sim.getShapeInertia(int shapeHandle)"""
        ...

    def getShapeMass(self, shapeHandle: int) -> float:
        """float mass = sim.getShapeMass(int shapeHandle)"""
        ...

    def getShapeMesh(self, shapeHandle: int) -> Tuple[list, list, list]:
        """float[] vertices, int[] indices, float[] normals = sim.getShapeMesh(int shapeHandle)"""
        ...

    def getShapeTextureId(self, shapeHandle: int) -> int:
        """int textureId = sim.getShapeTextureId(int shapeHandle)"""
        ...

    def getShapeViz(self, shapeHandle: int, itemIndex: int) -> dict:
        """map data = sim.getShapeViz(int shapeHandle, int itemIndex)"""
        ...

    def getSignalName(self, signalIndex: int, signalType: int) -> str:
        """string signalName = sim.getSignalName(int signalIndex, int signalType)"""
        ...

    def getSimulationState(self) -> int:
        """int simulationState = sim.getSimulationState()"""
        ...

    def getSimulationStopping(self) -> bool:
        """bool stopping = sim.getSimulationStopping()"""
        ...

    def getSimulationTime(self) -> float:
        """float simulationTime = sim.getSimulationTime()"""
        ...

    def getSimulationTimeStep(self) -> float:
        """float timeStep = sim.getSimulationTimeStep()"""
        ...

    def getSimulatorMessage(self) -> Tuple[int, Any, list]:
        """int messageID, int[4] auxiliaryData, int[1..*] auxiliaryData2 = sim.getSimulatorMessage()"""
        ...

    def getStackTraceback(self, scriptHandle: int = sim.handle_self) -> str:
        """string stacktraceback = sim.getStackTraceback(int scriptHandle=sim.handle_self)"""
        ...

    def getStringParam(self, parameter: int) -> str:
        """string stringState = sim.getStringParam(int parameter)"""
        ...

    def getStringProperty(self, target: int, pName: str, options: dict = ...) -> str:
        """string pValue = sim.getStringProperty(int target, string pName, map options={})"""
        ...

    def getStringSignal(self, signalName: str) -> str:
        """string signalValue = sim.getStringSignal(string signalName)"""
        ...

    def getSystemTime(self) -> float:
        """float time = sim.getSystemTime()"""
        ...

    def getTableProperty(self, target: int, pName: str, options: dict = ...) -> dict:
        """map pValue = sim.getTableProperty(int target, string pName, map options={})"""
        ...

    def getTextureId(self, textureName: str) -> Tuple[int, Any]:
        """int textureId, int[2] resolution = sim.getTextureId(string textureName)"""
        ...

    def getThreadId(self) -> int:
        """int threadId = sim.getThreadId()"""
        ...

    def getUserVariables(self) -> list:
        """string[] variables = sim.getUserVariables()"""
        ...

    def getVector2Property(self, target: int, pName: str, options: dict = ...) -> Any:
        """float[2] pValue = sim.getVector2Property(int target, string pName, map options={})"""
        ...

    def getVector3Property(self, target: int, pName: str, options: dict = ...) -> Any:
        """float[3] pValue = sim.getVector3Property(int target, string pName, map options={})"""
        ...

    def getVelocity(self, shapeHandle: int) -> Tuple[Any, Any]:
        """float[3] linearVelocity, float[3] angularVelocity = sim.getVelocity(int shapeHandle)"""
        ...

    def getVisionSensorDepth(self, sensorHandle: int, options: int = 0, pos: Any = ..., arg3: Any, size: Any = ..., arg5: Any) -> Tuple[bytes, Any]:
        """buffer depth, int[2] resolution = sim.getVisionSensorDepth(int sensorHandle, int options=0, int[2] pos={0, 0}, int[2] size={0, 0})"""
        ...

    def getVisionSensorImg(self, sensorHandle: int, options: int = 0, rgbaCutOff: float = 0.0, pos: Any = ..., arg4: Any, size: Any = ..., arg6: Any) -> Tuple[bytes, Any]:
        """buffer image, int[2] resolution = sim.getVisionSensorImg(int sensorHandle, int options=0, float rgbaCutOff=0.0, int[2] pos={0, 0}, int[2] size={0, 0})"""
        ...

    def getVisionSensorRes(self, sensorHandle: int) -> None:
        """sim.getVisionSensorRes(int sensorHandle)"""
        ...

    def groupShapes(self, shapeHandles: list, merge: bool = false) -> int:
        """int shapeHandle = sim.groupShapes(int[] shapeHandles, bool merge=false)"""
        ...

    def handleAddOnScripts(self, callType: int) -> int:
        """int count = sim.handleAddOnScripts(int callType)"""
        ...

    def handleDynamics(self, deltaTime: float) -> int:
        """int result = sim.handleDynamics(float deltaTime)"""
        ...

    def handleEmbeddedScripts(self, callType: int) -> int:
        """int calledScripts = sim.handleEmbeddedScripts(int callType)"""
        ...

    def handleExtCalls(self) -> None:
        """sim.handleExtCalls()"""
        ...

    def handleGraph(self, objectHandle: int, simulationTime: float) -> None:
        """sim.handleGraph(int objectHandle, float simulationTime)"""
        ...

    def handleJointMotion(self) -> None:
        """sim.handleJointMotion()"""
        ...

    def handleProximitySensor(self, sensorHandle: int) -> Tuple[int, float, Any, int, Any]:
        """int result, float distance, float[3] detectedPoint, int detectedObjectHandle, float[3] normalVector = sim.handleProximitySensor(int sensorHandle)"""
        ...

    def handleSandboxScript(self, callType: int) -> None:
        """sim.handleSandboxScript(int callType)"""
        ...

    def handleSensingStart(self) -> None:
        """sim.handleSensingStart()"""
        ...

    def handleSimulationScripts(self, callType: int) -> int:
        """int calledScripts = sim.handleSimulationScripts(int callType)"""
        ...

    def handleSimulationStart(self) -> None:
        """sim.handleSimulationStart()"""
        ...

    def handleVisionSensor(self, sensorHandle: int) -> Tuple[int, list, list]:
        """int detectionCount, float[] auxPacket1, float[] auxPacket2 = sim.handleVisionSensor(int sensorHandle)"""
        ...

    def importMesh(self, fileformat: int, pathAndFilename: str, options: int, identicalVerticeTolerance: float, scalingFactor: float) -> Tuple[list, list]:
        """float[1..*] vertices, int[1..*] indices = sim.importMesh(int fileformat, string pathAndFilename, int options, float identicalVerticeTolerance, float scalingFactor)"""
        ...

    def importShape(self, fileformat: int, pathAndFilename: str, options: int, identicalVerticeTolerance: float, scalingFactor: float) -> int:
        """int shapeHandle = sim.importShape(int fileformat, string pathAndFilename, int options, float identicalVerticeTolerance, float scalingFactor)"""
        ...

    def initScript(self, scriptHandle: int) -> None:
        """sim.initScript(int scriptHandle)"""
        ...

    def insertObjectIntoOctree(self, octreeHandle: int, objectHandle: int, options: int, color: list = nil, tag: int = 0) -> int:
        """int totalVoxelCnt = sim.insertObjectIntoOctree(int octreeHandle, int objectHandle, int options, float[] color=nil, int tag=0)"""
        ...

    def insertObjectIntoPointCloud(self, pointCloudHandle: int, objectHandle: int, options: int, gridSize: float, color: list = nil, duplicateTolerance: float = nil) -> int:
        """int totalPointCnt = sim.insertObjectIntoPointCloud(int pointCloudHandle, int objectHandle, int options, float gridSize, float[] color=nil, float duplicateTolerance=nil)"""
        ...

    def insertPointsIntoPointCloud(self, pointCloudHandle: int, options: int, points: list, color: list = nil, duplicateTolerance: float = nil) -> int:
        """int totalPointCnt = sim.insertPointsIntoPointCloud(int pointCloudHandle, int options, float[] points, float[] color=nil, float duplicateTolerance=nil)"""
        ...

    def insertVoxelsIntoOctree(self, octreeHandle: int, options: int, points: list, color: list = nil, tag: list = nil) -> int:
        """int totalVoxelCnt = sim.insertVoxelsIntoOctree(int octreeHandle, int options, float[] points, float[] color=nil, int[] tag=nil)"""
        ...

    def interpolateMatrices(self, matrixIn1: Any, matrixIn2: Any, interpolFactor: float) -> Any:
        """float[12] resultMatrix = sim.interpolateMatrices(float[12] matrixIn1, float[12] matrixIn2, float interpolFactor)"""
        ...

    def interpolatePoses(self, poseIn1: Any, poseIn2: Any, interpolFactor: float) -> Any:
        """float[7] resultPose = sim.interpolatePoses(float[7] poseIn1, float[7] poseIn2, float interpolFactor)"""
        ...

    def intersectPointsWithPointCloud(self, pointCloudHandle: int, options: int, points: list, tolerance: float) -> int:
        """int totalPointCnt = sim.intersectPointsWithPointCloud(int pointCloudHandle, int options, float[] points, float tolerance)"""
        ...

    def isDeprecated(self, funcOrConst: str) -> int:
        """int result = sim.isDeprecated(string funcOrConst)"""
        ...

    def isDynamicallyEnabled(self, objectHandle: int) -> bool:
        """bool enabled = sim.isDynamicallyEnabled(int objectHandle)"""
        ...

    def isHandle(self, objectHandle: int) -> bool:
        """bool result = sim.isHandle(int objectHandle)"""
        ...

    def isPluginLoaded(self, name: str) -> bool:
        """bool loaded = sim.isPluginLoaded(string name)"""
        ...

    def launchExecutable(self) -> Tuple[Any, str]:
        """sim.launchExecutable(string filename, string parameters='', int showStatus=1)"""
        ...

    def loadImage(self, options: int, filename: str) -> Tuple[bytes, Any]:
        """buffer image, int[2] resolution = sim.loadImage(int options, string filename)"""
        ...

    def loadModel(self, filename: str) -> int:
        """int objectHandle = sim.loadModel(string filename)"""
        ...

    def loadPlugin(self, name: str) -> int:
        """int handle = sim.loadPlugin(string name)"""
        ...

    def loadScene(self, filename: str) -> None:
        """sim.loadScene(string filename)"""
        ...

    def matrixToPose(self, matrix: Any) -> Any:
        """float[7] pose = sim.matrixToPose(float[12] matrix)"""
        ...

    def moduleEntry(self, handle: int, label: str = nil, state: int = -1) -> int:
        """int handle = sim.moduleEntry(int handle, string label=nil, int state=-1)"""
        ...

    def moveToConfig(self, params: dict) -> dict:
        """map data = sim.moveToConfig(map params)"""
        ...

    def moveToConfig_cleanup(self, motionObject: dict) -> None:
        """sim.moveToConfig_cleanup(map motionObject)"""
        ...

    def moveToConfig_init(self, params: dict) -> dict:
        """map motionObject = sim.moveToConfig_init(map params)"""
        ...

    def moveToConfig_step(self, motionObject: dict) -> Tuple[int, dict]:
        """int res, map data = sim.moveToConfig_step(map motionObject)"""
        ...

    def moveToPose(self, params: dict) -> dict:
        """map data = sim.moveToPose(map params)"""
        ...

    def moveToPose_cleanup(self, motionObject: dict) -> None:
        """sim.moveToPose_cleanup(map motionObject)"""
        ...

    def moveToPose_init(self, params: dict) -> dict:
        """map motionObject = sim.moveToPose_init(map params)"""
        ...

    def moveToPose_step(self, motionObject: dict) -> Tuple[int, dict]:
        """int res, map data = sim.moveToPose_step(map motionObject)"""
        ...

    def multiplyMatrices(self, matrixIn1: Any, matrixIn2: Any) -> Any:
        """float[12] resultMatrix = sim.multiplyMatrices(float[12] matrixIn1, float[12] matrixIn2)"""
        ...

    def multiplyPoses(self, poseIn1: Any, poseIn2: Any) -> Any:
        """float[7] resultPose = sim.multiplyPoses(float[7] poseIn1, float[7] poseIn2)"""
        ...

    def multiplyVector(self, matrix: Any, inVectors: list) -> list:
        """float[] resultVectors = sim.multiplyVector(float[12] matrix, float[] inVectors)"""
        ...

    def packDoubleTable(self, doubleNumbers: list, startDoubleIndex: int = 0, doubleCount: int = 0) -> bytes:
        """buffer data = sim.packDoubleTable(float[] doubleNumbers, int startDoubleIndex=0, int doubleCount=0)"""
        ...

    def packFloatTable(self, floatNumbers: list, startFloatIndex: int = 0, floatCount: int = 0) -> bytes:
        """buffer data = sim.packFloatTable(float[] floatNumbers, int startFloatIndex=0, int floatCount=0)"""
        ...

    def packInt32Table(self, int32Numbers: list, startInt32Index: int = 0, int32Count: int = 0) -> bytes:
        """buffer data = sim.packInt32Table(int[] int32Numbers, int startInt32Index=0, int int32Count=0)"""
        ...

    def packTable(self, aTable: list, scheme: int = 0) -> bytes:
        """buffer data = sim.packTable(any[] aTable, int scheme=0)"""
        ...

    def packUInt16Table(self, uint16Numbers: list, startUint16Index: int = 0, uint16Count: int = 0) -> bytes:
        """buffer data = sim.packUInt16Table(int[] uint16Numbers, int startUint16Index=0, int uint16Count=0)"""
        ...

    def packUInt32Table(self, uint32Numbers: list, startUInt32Index: int = 0, uint32Count: int = 0) -> bytes:
        """buffer data = sim.packUInt32Table(int[] uint32Numbers, int startUInt32Index=0, int uint32Count=0)"""
        ...

    def packUInt8Table(self, uint8Numbers: list, startUint8Index: int = 0, uint8count: int = 0) -> bytes:
        """buffer data = sim.packUInt8Table(int[] uint8Numbers, int startUint8Index=0, int uint8count=0)"""
        ...

    def pauseSimulation(self) -> None:
        """sim.pauseSimulation()"""
        ...

    def poseToMatrix(self, pose: Any) -> Any:
        """float[12] matrix = sim.poseToMatrix(float[7] pose)"""
        ...

    def pushUserEvent(self) -> Tuple[Any, int, int, dict, int]:
        """sim.pushUserEvent(string event, int handle, int uid, map eventData, int options=0)"""
        ...

    def quitSimulator(self) -> None:
        """sim.quitSimulator()"""
        ...

    def readCustomBufferData(self, objectHandle: int, tagName: str) -> bytes:
        """buffer data = sim.readCustomBufferData(int objectHandle, string tagName)"""
        ...

    def readCustomDataBlockEx(self, handle: int, tag: str, options: dict = ...) -> Tuple[bytes, str]:
        """buffer data, string dataType = sim.readCustomDataBlockEx(int handle, string tag, map options={})"""
        ...

    def readCustomDataTags(self, objectHandle: int) -> list:
        """string[] tags = sim.readCustomDataTags(int objectHandle)"""
        ...

    def readCustomStringData(self, objectHandle: int, tagName: str) -> str:
        """string data = sim.readCustomStringData(int objectHandle, string tagName)"""
        ...

    def readCustomTableData(self, handle: int, tagName: str, options: dict = ...) -> dict:
        """map data = sim.readCustomTableData(int handle, string tagName, map options={})"""
        ...

    def readForceSensor(self, objectHandle: int) -> Tuple[int, Any, Any]:
        """int result, float[3] forceVector, float[3] torqueVector = sim.readForceSensor(int objectHandle)"""
        ...

    def readProximitySensor(self, sensorHandle: int) -> Tuple[int, float, Any, int, Any]:
        """int result, float distance, float[3] detectedPoint, int detectedObjectHandle, float[3] normalVector = sim.readProximitySensor(int sensorHandle)"""
        ...

    def readTexture(self, textureId: int, options: int, posX: int = 0, posY: int = 0, sizeX: int = 0, sizeY: int = 0) -> bytes:
        """buffer textureData = sim.readTexture(int textureId, int options, int posX=0, int posY=0, int sizeX=0, int sizeY=0)"""
        ...

    def readVisionSensor(self, sensorHandle: int) -> Tuple[int, list, list]:
        """int result, float[] auxPacket1, float[] auxPacket2 = sim.readVisionSensor(int sensorHandle)"""
        ...

    def refreshDialogs(self, refreshDegree: int) -> int:
        """int result = sim.refreshDialogs(int refreshDegree)"""
        ...

    def registerScriptFuncHook(self, funcToHook: str, userFunc: Any, execBefore: bool) -> int:
        """int result = sim.registerScriptFuncHook(string funcToHook, func userFunc, bool execBefore)"""
        ...

    def releaseLock(self) -> None:
        """sim.releaseLock()"""
        ...

    def relocateShapeFrame(self, shapeHandle: int, pose: Any) -> int:
        """int result = sim.relocateShapeFrame(int shapeHandle, float[7] pose)"""
        ...

    def removeDrawingObject(self, drawingObjectHandle: int) -> None:
        """sim.removeDrawingObject(int drawingObjectHandle)"""
        ...

    def removeModel(self, objectHandle: int, delayedRemoval: bool = false) -> int:
        """int objectCount = sim.removeModel(int objectHandle, bool delayedRemoval=false)"""
        ...

    def removeObjects(self) -> Tuple[list, bool]:
        """sim.removeObjects(int[1..*] objectHandles, bool delayedRemoval=false)"""
        ...

    def removeParticleObject(self, particleObjectHandle: int) -> None:
        """sim.removeParticleObject(int particleObjectHandle)"""
        ...

    def removePointsFromPointCloud(self, pointCloudHandle: int, options: int, points: list, tolerance: float) -> int:
        """int totalPointCnt = sim.removePointsFromPointCloud(int pointCloudHandle, int options, float[] points, float tolerance)"""
        ...

    def removeProperty(self) -> Tuple[Any, str, dict]:
        """sim.removeProperty(int target, string pName, map options={})"""
        ...

    def removeReferencedObjects(self) -> Tuple[Any, str]:
        """sim.removeReferencedObjects(int objectHandle, string tag='')"""
        ...

    def removeVoxelsFromOctree(self, octreeHandle: int, options: int, points: list) -> int:
        """int totalVoxelCnt = sim.removeVoxelsFromOctree(int octreeHandle, int options, float[] points)"""
        ...

    # Could not generate stub for: sim.resamplePath
    # Original signature: float[] path = sim.resamplePath(float[] path, float[] pathLengths, int finalConfigCnt, map method={type='linear', strength=1.0, forceOpen=false}, int[] types=nil)

    def resetDynamicObject(self, objectHandle: int) -> None:
        """sim.resetDynamicObject(int objectHandle)"""
        ...

    def resetGraph(self, objectHandle: int) -> None:
        """sim.resetGraph(int objectHandle)"""
        ...

    def resetProximitySensor(self, objectHandle: int) -> None:
        """sim.resetProximitySensor(int objectHandle)"""
        ...

    def resetVisionSensor(self, sensorHandle: int) -> None:
        """sim.resetVisionSensor(int sensorHandle)"""
        ...

    def restoreEntityColor(self, originalColorData: list) -> None:
        """sim.restoreEntityColor(map[] originalColorData)"""
        ...

    def rotateAroundAxis(self, matrixIn: Any, axis: Any, axisPos: Any, angle: float) -> Any:
        """float[12] matrixOut = sim.rotateAroundAxis(float[12] matrixIn, float[3] axis, float[3] axisPos, float angle)"""
        ...

    def ruckigPos(self, dofs: int, baseCycleTime: float, flags: int, currentPosVelAccel: list, maxVelAccelJerk: list, selection: list, targetPosVel: list) -> int:
        """int handle = sim.ruckigPos(int dofs, float baseCycleTime, int flags, float[] currentPosVelAccel, float[] maxVelAccelJerk, int[] selection, float[] targetPosVel)"""
        ...

    def ruckigRemove(self, handle: int) -> None:
        """sim.ruckigRemove(int handle)"""
        ...

    def ruckigStep(self, handle: int, cycleTime: float) -> Tuple[int, list, float]:
        """int result, float[] newPosVelAccel, float synchronizationTime = sim.ruckigStep(int handle, float cycleTime)"""
        ...

    def ruckigVel(self, dofs: int, baseCycleTime: float, flags: int, currentPosVelAccel: list, maxAccelJerk: list, selection: list, targetVel: list) -> int:
        """int handle = sim.ruckigVel(int dofs, float baseCycleTime, int flags, float[] currentPosVelAccel, float[] maxAccelJerk, int[] selection, float[] targetVel)"""
        ...

    def saveImage(self, image: bytes, resolution: Any, options: int, filename: str, quality: int) -> bytes:
        """buffer serializedImage = sim.saveImage(buffer image, int[2] resolution, int options, string filename, int quality)"""
        ...

    def saveModel(self, modelBaseHandle: int, filename: str) -> None:
        """sim.saveModel(int modelBaseHandle, string filename)"""
        ...

    def saveScene(self, filename: str) -> None:
        """sim.saveScene(string filename)"""
        ...

    def scaleObject(self) -> Tuple[Any, float, float, float, int]:
        """sim.scaleObject(int objectHandle, float xScale, float yScale, float zScale, int options=0)"""
        ...

    def scaleObjects(self, objectHandles: list, scalingFactor: float, scalePositionsToo: bool) -> None:
        """sim.scaleObjects(int[1..*] objectHandles, float scalingFactor, bool scalePositionsToo)"""
        ...

    def scheduleExecution(self, f: Any, args: list, timePoint: float, simTime: bool = false) -> int:
        """int id = sim.scheduleExecution(func f, any[] args, float timePoint, bool simTime=false)"""
        ...

    def serialCheck(self, portHandle: int) -> int:
        """int byteCount = sim.serialCheck(int portHandle)"""
        ...

    def serialClose(self, portHandle: int) -> None:
        """sim.serialClose(int portHandle)"""
        ...

    def serialOpen(self, portString: str, baudrate: int) -> int:
        """int portHandle = sim.serialOpen(string portString, int baudrate)"""
        ...

    def serialRead(self, portHandle: int, dataLengthToRead: int, blockingOperation: bool, closingString: bytes = '', timeout: float = 0) -> bytes:
        """buffer data = sim.serialRead(int portHandle, int dataLengthToRead, bool blockingOperation, buffer closingString='', float timeout=0)"""
        ...

    def serialSend(self, portHandle: int, data: bytes) -> int:
        """int charsSent = sim.serialSend(int portHandle, buffer data)"""
        ...

    def setArrayParam(self, parameter: int, arrayOfValues: Any) -> None:
        """sim.setArrayParam(int parameter, float[3] arrayOfValues)"""
        ...

    def setAutoYieldDelay(self, dt: float) -> None:
        """sim.setAutoYieldDelay(float dt)"""
        ...

    def setBoolParam(self, parameter: int, boolState: bool) -> None:
        """sim.setBoolParam(int parameter, bool boolState)"""
        ...

    def setBoolProperty(self) -> Tuple[Any, str, bool, dict]:
        """sim.setBoolProperty(int target, string pName, bool pValue, map options={})"""
        ...

    def setBufferProperty(self) -> Tuple[Any, str, bytes, dict]:
        """sim.setBufferProperty(int target, string pName, buffer pValue, map options={})"""
        ...

    def setBufferSignal(self, signalName: str, signalValue: bytes) -> None:
        """sim.setBufferSignal(string signalName, buffer signalValue)"""
        ...

    def setColorProperty(self) -> Tuple[Any, str, Any, dict]:
        """sim.setColorProperty(int target, string pName, float[3] pValue, map options={})"""
        ...

    def setEngineBoolParam(self, paramId: int, objectHandle: int, boolParam: bool) -> None:
        """sim.setEngineBoolParam(int paramId, int objectHandle, bool boolParam)"""
        ...

    def setEngineFloatParam(self, paramId: int, objectHandle: int, floatParam: float) -> None:
        """sim.setEngineFloatParam(int paramId, int objectHandle, float floatParam)"""
        ...

    def setEngineInt32Param(self, paramId: int, objectHandle: int, int32Param: int) -> None:
        """sim.setEngineInt32Param(int paramId, int objectHandle, int int32Param)"""
        ...

    def setEventFilters(self) -> Any:
        """sim.setEventFilters(map filters={})"""
        ...

    def setExplicitHandling(self, objectHandle: int, explicitHandlingFlags: int) -> None:
        """sim.setExplicitHandling(int objectHandle, int explicitHandlingFlags)"""
        ...

    def setFloatArrayProperty(self) -> Tuple[Any, str, list, dict]:
        """sim.setFloatArrayProperty(int target, string pName, float[] pValue, map options={})"""
        ...

    def setFloatParam(self, parameter: int, floatState: float) -> None:
        """sim.setFloatParam(int parameter, float floatState)"""
        ...

    def setFloatProperty(self) -> Tuple[Any, str, float, dict]:
        """sim.setFloatProperty(int target, string pName, float pValue, map options={})"""
        ...

    def setFloatSignal(self, signalName: str, signalValue: float) -> None:
        """sim.setFloatSignal(string signalName, float signalValue)"""
        ...

    def setGraphStreamTransformation(self) -> Tuple[Any, int, int, float]:
        """sim.setGraphStreamTransformation(int graphHandle, int streamId, int trType, float mult=1.0, float off=0.0, int movAvgPeriod=1)"""
        ...

    def setGraphStreamValue(self, graphHandle: int, streamId: int, value: float) -> None:
        """sim.setGraphStreamValue(int graphHandle, int streamId, float value)"""
        ...

    def setInt32Param(self, parameter: int, intState: int) -> None:
        """sim.setInt32Param(int parameter, int intState)"""
        ...

    def setInt32Signal(self, signalName: str, signalValue: int) -> None:
        """sim.setInt32Signal(string signalName, int signalValue)"""
        ...

    def setIntArray2Property(self) -> Tuple[Any, str, Any, dict]:
        """sim.setIntArray2Property(int target, string pName, int[2] pValue, map options={})"""
        ...

    def setIntArrayProperty(self) -> Tuple[Any, str, list, dict]:
        """sim.setIntArrayProperty(int target, string pName, int[] pValue, map options={})"""
        ...

    def setIntProperty(self) -> Tuple[Any, str, int, dict]:
        """sim.setIntProperty(int target, string pName, int pValue, map options={})"""
        ...

    def setJointDependency(self, jointHandle: int, masterJointHandle: int, offset: float, multCoeff: float) -> None:
        """sim.setJointDependency(int jointHandle, int masterJointHandle, float offset, float multCoeff)"""
        ...

    def setJointInterval(self, objectHandle: int, cyclic: bool, interval: Any) -> None:
        """sim.setJointInterval(int objectHandle, bool cyclic, float[2] interval)"""
        ...

    def setJointMode(self, jointHandle: int, jointMode: int) -> None:
        """sim.setJointMode(int jointHandle, int jointMode)"""
        ...

    def setJointPosition(self, objectHandle: int, position: float) -> None:
        """sim.setJointPosition(int objectHandle, float position)"""
        ...

    def setJointTargetForce(self) -> Tuple[Any, float, bool]:
        """sim.setJointTargetForce(int objectHandle, float forceOrTorque, bool signedValue=true)"""
        ...

    def setJointTargetPosition(self) -> Tuple[Any, float, list]:
        """sim.setJointTargetPosition(int objectHandle, float targetPosition, float[] motionParams={})"""
        ...

    def setJointTargetVelocity(self) -> Tuple[Any, float, list]:
        """sim.setJointTargetVelocity(int objectHandle, float targetVelocity, float[] motionParams={})"""
        ...

    def setLightParameters(self, lightHandle: int, state: int, reserved: Any, diffusePart: Any, specularPart: Any) -> None:
        """sim.setLightParameters(int lightHandle, int state, float[3] reserved, float[3] diffusePart, float[3] specularPart)"""
        ...

    def setLinkDummy(self, dummyHandle: int, linkDummyHandle: int) -> None:
        """sim.setLinkDummy(int dummyHandle, int linkDummyHandle)"""
        ...

    def setLongProperty(self) -> Tuple[Any, str, int, dict]:
        """sim.setLongProperty(int target, string pName, int pValue, map options={})"""
        ...

    def setModelProperty(self, objectHandle: int, property: int) -> None:
        """sim.setModelProperty(int objectHandle, int property)"""
        ...

    def setNamedBoolParam(self, name: str, value: bool) -> None:
        """sim.setNamedBoolParam(string name, bool value)"""
        ...

    def setNamedFloatParam(self, name: str, value: float) -> None:
        """sim.setNamedFloatParam(string name, float value)"""
        ...

    def setNamedInt32Param(self, name: str, value: int) -> None:
        """sim.setNamedInt32Param(string name, int value)"""
        ...

    def setNamedStringParam(self, paramName: str, stringParam: bytes) -> None:
        """sim.setNamedStringParam(string paramName, buffer stringParam)"""
        ...

    def setNavigationMode(self, navigationMode: int) -> None:
        """sim.setNavigationMode(int navigationMode)"""
        ...

    def setObjectAlias(self, objectHandle: int, objectAlias: str) -> None:
        """sim.setObjectAlias(int objectHandle, string objectAlias)"""
        ...

    def setObjectChildPose(self, objectHandle: int, pose: Any) -> None:
        """sim.setObjectChildPose(int objectHandle, float[7] pose)"""
        ...

    def setObjectColor(self, objectHandle: int, index: int, colorComponent: int, rgbData: Any) -> bool:
        """bool result = sim.setObjectColor(int objectHandle, int index, int colorComponent, float[3] rgbData)"""
        ...

    def setObjectFloatArrayParam(self, objectHandle: int, parameterID: int, params: list) -> None:
        """sim.setObjectFloatArrayParam(int objectHandle, int parameterID, float[] params)"""
        ...

    def setObjectFloatParam(self, objectHandle: int, parameterID: int, parameter: float) -> None:
        """sim.setObjectFloatParam(int objectHandle, int parameterID, float parameter)"""
        ...

    def setObjectHierarchyOrder(self, objectHandle: int, order: int) -> None:
        """sim.setObjectHierarchyOrder(int objectHandle, int order)"""
        ...

    def setObjectInt32Param(self, objectHandle: int, parameterID: int, parameter: int) -> None:
        """sim.setObjectInt32Param(int objectHandle, int parameterID, int parameter)"""
        ...

    def setObjectMatrix(self) -> Tuple[Any, Any, int]:
        """sim.setObjectMatrix(int objectHandle, float[12] matrix, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def setObjectOrientation(self) -> Tuple[Any, Any, int]:
        """sim.setObjectOrientation(int objectHandle, float[3] eulerAngles, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def setObjectParent(self) -> Tuple[Any, int, bool]:
        """sim.setObjectParent(int objectHandle, int parentObjectHandle, bool keepInPlace=true)"""
        ...

    def setObjectPose(self) -> Tuple[Any, Any, int]:
        """sim.setObjectPose(int objectHandle, float[7] pose, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def setObjectPosition(self) -> Tuple[Any, Any, int]:
        """sim.setObjectPosition(int objectHandle, float[3] position, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def setObjectProperty(self, objectHandle: int, property: int) -> None:
        """sim.setObjectProperty(int objectHandle, int property)"""
        ...

    def setObjectQuaternion(self) -> Tuple[Any, Any, int]:
        """sim.setObjectQuaternion(int objectHandle, float[4] quaternion, int relativeToObjectHandle=sim.handle_world)"""
        ...

    def setObjectSel(self, objectHandles: list) -> None:
        """sim.setObjectSel(int[] objectHandles)"""
        ...

    def setObjectSpecialProperty(self, objectHandle: int, property: int) -> None:
        """sim.setObjectSpecialProperty(int objectHandle, int property)"""
        ...

    def setObjectStringParam(self, objectHandle: int, parameterID: int, parameter: bytes) -> None:
        """sim.setObjectStringParam(int objectHandle, int parameterID, buffer parameter)"""
        ...

    def setPage(self, pageIndex: int) -> None:
        """sim.setPage(int pageIndex)"""
        ...

    def setPluginInfo(self, pluginName: str, infoType: int, info: str) -> None:
        """sim.setPluginInfo(string pluginName, int infoType, string info)"""
        ...

    def setPointCloudOptions(self, pointCloudHandle: int, maxVoxelSize: float, maxPtCntPerVoxel: int, options: int, pointSize: float) -> None:
        """sim.setPointCloudOptions(int pointCloudHandle, float maxVoxelSize, int maxPtCntPerVoxel, int options, float pointSize)"""
        ...

    def setPoseProperty(self) -> Tuple[Any, str, Any, dict]:
        """sim.setPoseProperty(int target, string pName, float[7] pValue, map options={})"""
        ...

    def setProperties(self, target: int, props: dict) -> None:
        """sim.setProperties(int target, map props)"""
        ...

    def setProperty(self) -> Tuple[Any, str, Any, int]:
        """sim.setProperty(int target, string pName, any pValue, int pType=nil)"""
        ...

    def setQuaternionProperty(self) -> Tuple[Any, str, Any, dict]:
        """sim.setQuaternionProperty(int target, string pName, float[4] pValue, map options={})"""
        ...

    def setReferencedHandles(self) -> Tuple[Any, list, str]:
        """sim.setReferencedHandles(int objectHandle, int[] referencedHandles, string tag='')"""
        ...

    def setShapeAppearance(self, handle: int, savedData: dict, opts: dict = ...) -> int:
        """int handle = sim.setShapeAppearance(int handle, map savedData, map opts={})"""
        ...

    def setShapeBB(self, shapeHandle: int, size: Any) -> None:
        """sim.setShapeBB(int shapeHandle, float[3] size)"""
        ...

    def setShapeColor(self, shapeHandle: int, colorName: str, colorComponent: int, rgbData: Any) -> None:
        """sim.setShapeColor(int shapeHandle, string colorName, int colorComponent, float[3] rgbData)"""
        ...

    def setShapeInertia(self, shapeHandle: int, inertiaMatrix: Any, comMatrix: Any) -> None:
        """sim.setShapeInertia(int shapeHandle, float[9] inertiaMatrix, float[12] comMatrix)"""
        ...

    def setShapeMass(self, shapeHandle: int, mass: float) -> None:
        """sim.setShapeMass(int shapeHandle, float mass)"""
        ...

    def setShapeMaterial(self, shapeHandle: int, materialIdOrShapeHandle: int) -> None:
        """sim.setShapeMaterial(int shapeHandle, int materialIdOrShapeHandle)"""
        ...

    def setShapeTexture(self) -> Tuple[Any, int, int, int, Any, Any]:
        """sim.setShapeTexture(int shapeHandle, int textureId, int mappingMode, int options, float[2] uvScaling, float[3] position=nil, float[3] orientation=nil)"""
        ...

    def setStepping(self, enabled: bool) -> int:
        """int prevStepLevel = sim.setStepping(bool enabled)"""
        ...

    def setStringParam(self, parameter: int, stringState: str) -> None:
        """sim.setStringParam(int parameter, string stringState)"""
        ...

    def setStringProperty(self) -> Tuple[Any, str, str, dict]:
        """sim.setStringProperty(int target, string pName, string pValue, map options={})"""
        ...

    def setStringSignal(self, signalName: str, signalValue: str) -> None:
        """sim.setStringSignal(string signalName, string signalValue)"""
        ...

    def setTableProperty(self) -> Tuple[Any, str, dict, dict]:
        """sim.setTableProperty(int target, string pName, map pValue, map options={})"""
        ...

    def setVector2Property(self) -> Tuple[Any, str, Any, dict]:
        """sim.setVector2Property(int target, string pName, float[2] pValue, map options={})"""
        ...

    def setVector3Property(self) -> Tuple[Any, str, Any, dict]:
        """sim.setVector3Property(int target, string pName, float[3] pValue, map options={})"""
        ...

    def setVisionSensorImg(self) -> Tuple[Any, bytes, int]:
        """sim.setVisionSensorImg(int sensorHandle, buffer image, int options=0, int[2] pos={0, 0}, int[2] size={0, 0})"""
        ...

    def startSimulation(self) -> None:
        """sim.startSimulation()"""
        ...

    def step(self) -> None:
        """sim.step()"""
        ...

    def stopSimulation(self) -> Any:
        """sim.stopSimulation(bool wait=false)"""
        ...

    def subtractObjectFromOctree(self, octreeHandle: int, objectHandle: int, options: int) -> int:
        """int totalVoxelCnt = sim.subtractObjectFromOctree(int octreeHandle, int objectHandle, int options)"""
        ...

    def subtractObjectFromPointCloud(self, pointCloudHandle: int, objectHandle: int, options: int, tolerance: float) -> int:
        """int totalPointCnt = sim.subtractObjectFromPointCloud(int pointCloudHandle, int objectHandle, int options, float tolerance)"""
        ...

    def systemSemaphore(self, key: str, acquire: bool) -> None:
        """sim.systemSemaphore(string key, bool acquire)"""
        ...

    def testCB(self, a: int, cb: Any, b: int) -> int:
        """int ret = sim.testCB(int a, func cb, int b)"""
        ...

    def textEditorClose(self, handle: int) -> Tuple[str, Any, Any]:
        """string text, int[2] pos, int[2] size = sim.textEditorClose(int handle)"""
        ...

    def textEditorGetInfo(self, handle: int) -> Tuple[str, Any, Any, bool]:
        """string text, int[2] pos, int[2] size, bool visible = sim.textEditorGetInfo(int handle)"""
        ...

    def textEditorOpen(self, initText: str, properties: str) -> int:
        """int handle = sim.textEditorOpen(string initText, string properties)"""
        ...

    def textEditorShow(self, handle: int, showState: bool) -> None:
        """sim.textEditorShow(int handle, bool showState)"""
        ...

    def throttle(self, period: float, f: Any, *args) -> None:
        """sim.throttle(float period, func f, ...)"""
        ...

    def transformBuffer(self, inBuffer: bytes, inFormat: int, multiplier: float, offset: float, outFormat: int) -> bytes:
        """buffer outBuffer = sim.transformBuffer(buffer inBuffer, int inFormat, float multiplier, float offset, int outFormat)"""
        ...

    def transformImage(self, image: bytes, resolution: Any, options: int) -> bytes:
        """buffer newImage = sim.transformImage(buffer image, int[2] resolution, int options)"""
        ...

    def ungroupShape(self, shapeHandle: int) -> list:
        """int[] simpleShapeHandles = sim.ungroupShape(int shapeHandle)"""
        ...

    def unpackDoubleTable(self, data: bytes, startDoubleIndex: int = 0, doubleCount: int = 0, additionalByteOffset: int = 0) -> list:
        """float[] doubleNumbers = sim.unpackDoubleTable(buffer data, int startDoubleIndex=0, int doubleCount=0, int additionalByteOffset=0)"""
        ...

    def unpackFloatTable(self, data: bytes, startFloatIndex: int = 0, floatCount: int = 0, additionalByteOffset: int = 0) -> list:
        """float[] floatNumbers = sim.unpackFloatTable(buffer data, int startFloatIndex=0, int floatCount=0, int additionalByteOffset=0)"""
        ...

    def unpackInt32Table(self, data: bytes, startInt32Index: int = 0, int32Count: int = 0, additionalByteOffset: int = 0) -> list:
        """int[] int32Numbers = sim.unpackInt32Table(buffer data, int startInt32Index=0, int int32Count=0, int additionalByteOffset=0)"""
        ...

    def unpackTable(self, buffer: bytes) -> Any:
        """any aTable = sim.unpackTable(buffer buffer)"""
        ...

    def unpackUInt16Table(self, data: bytes, startUint16Index: int = 0, uint16Count: int = 0, additionalByteOffset: int = 0) -> list:
        """int[] uint16Numbers = sim.unpackUInt16Table(buffer data, int startUint16Index=0, int uint16Count=0, int additionalByteOffset=0)"""
        ...

    def unpackUInt32Table(self, data: bytes, startUint32Index: int = 0, uint32Count: int = 0, additionalByteOffset: int = 0) -> list:
        """int[] uint32Numbers = sim.unpackUInt32Table(buffer data, int startUint32Index=0, int uint32Count=0, int additionalByteOffset=0)"""
        ...

    def unpackUInt8Table(self, data: bytes, startUint8Index: int = 0, uint8count: int = 0) -> list:
        """int[] uint8Numbers = sim.unpackUInt8Table(buffer data, int startUint8Index=0, int uint8count=0)"""
        ...

    def visitTree(self) -> Tuple[Any, Any, dict]:
        """sim.visitTree(int rootHandle, func visitorFunc, map options={})"""
        ...

    def wait(self, dt: float, simulationTime: bool = true) -> float:
        """float timeLeft = sim.wait(float dt, bool simulationTime=true)"""
        ...

    def waitForSignal(self, target: int, sigName: str) -> Any:
        """any sigVal = sim.waitForSignal(int target, string sigName)"""
        ...

    def writeCustomBufferData(self, objectHandle: int, tagName: str, data: bytes) -> None:
        """sim.writeCustomBufferData(int objectHandle, string tagName, buffer data)"""
        ...

    def writeCustomDataBlockEx(self) -> Tuple[Any, str, bytes, dict]:
        """sim.writeCustomDataBlockEx(int handle, string tag, buffer data, map options={})"""
        ...

    def writeCustomStringData(self, objectHandle: int, tagName: str, data: str) -> None:
        """sim.writeCustomStringData(int objectHandle, string tagName, string data)"""
        ...

    def writeCustomTableData(self) -> Tuple[Any, str, dict, dict]:
        """sim.writeCustomTableData(int handle, string tagName, map theTable, map options={})"""
        ...

    def writeTexture(self) -> Tuple[Any, int, bytes, int]:
        """sim.writeTexture(int textureId, int options, buffer textureData, int posX=0, int posY=0, int sizeX=0, int sizeY=0, float interpol=0.0)"""
        ...

    def yawPitchRollToAlphaBetaGamma(self, yawAngle: float, pitchAngle: float, rollAngle: float) -> Tuple[float, float, float]:
        """float alphaAngle, float betaAngle, float gammaAngle = sim.yawPitchRollToAlphaBetaGamma(float yawAngle, float pitchAngle, float rollAngle)"""
        ...

    def yield(self) -> None:
        """sim.yield()"""
        ...


class simAssimp:
    """API functions for the `simAssimp` module."""

    # --- Constants ---
    pluginHandle: int
    upVector_auto: int
    upVector_y: int
    upVector_z: int

    # --- Functions ---
    def exportMeshes(self) -> Tuple[Any, dict, str, str, float]:
        """simAssimp.exportMeshes(map allVertices, map allIndices, string filename, string formatId, float scaling=1.0, int upVector=simassimp_upvect_z, int options=0)"""
        ...

    def exportShapes(self) -> Tuple[list, str, str, float]:
        """simAssimp.exportShapes(int[] shapeHandles, string filename, string formatId, float scaling=1.0, int upVector=simassimp_upvect_z, int options=0)"""
        ...

    def exportShapesDlg(self, filename: str, shapeHandles: list) -> None:
        """simAssimp.exportShapesDlg(string filename, int[] shapeHandles)"""
        ...

    def getExportFormat(self, index: int) -> Tuple[str, str, str]:
        """string formatDescription, string formatExtension, string formatId = simAssimp.getExportFormat(int index)"""
        ...

    def getImportFormat(self, index: int) -> Tuple[str, str]:
        """string formatDescription, string formatExtension = simAssimp.getImportFormat(int index)"""
        ...

    def importMeshes(self, filenames: str, scaling: float = 0.0, upVector: int = simassimp_upvect_auto, options: int = 0) -> Tuple[dict, dict]:
        """map allVertices, map allIndices = simAssimp.importMeshes(string filenames, float scaling=0.0, int upVector=simassimp_upvect_auto, int options=0)"""
        ...

    def importShapes(self, filenames: str, maxTextureSize: int = 512, scaling: float = 0.0, upVector: int = simassimp_upvect_auto, options: int = 0) -> list:
        """int[] shapeHandles = simAssimp.importShapes(string filenames, int maxTextureSize=512, float scaling=0.0, int upVector=simassimp_upvect_auto, int options=0)"""
        ...

    def importShapesDlg(self, filename: str) -> list:
        """int[] handles = simAssimp.importShapesDlg(string filename)"""
        ...


class simBWF:
    """API functions for the `simBWF` module."""

    # --- Functions ---
    def query(self, command: str, data: dict) -> Tuple[str, dict]:
        """string status,map data=query(string command,map data)"""
        ...


class simBubble:
    """API functions for the `simBubble` module."""

    # --- Functions ---
    def create(self, motorJointHandles: Any, sensorHandle: int, backRelativeVelocities: Any) -> int:
        """int bubbleRobHandle = simBubble.create(int[2] motorJointHandles, int sensorHandle, float[2] backRelativeVelocities)"""
        ...

    def destroy(self, bubbleRobHandle: int) -> bool:
        """bool result = simBubble.destroy(int bubbleRobHandle)"""
        ...

    def start(self, bubbleRobHandle: int) -> bool:
        """bool result = simBubble.start(int bubbleRobHandle)"""
        ...

    def stop(self, bubbleRobHandle: int) -> bool:
        """bool result = simBubble.stop(int bubbleRobHandle)"""
        ...


class simCHAI3D:
    """API functions for the `simCHAI3D` module."""

    # --- Functions ---
    def addConstraintPlane(self, deviceIndex: int, position: Any, normal: Any, Kp: float, Kv: float, Fmax: float) -> int:
        """int objectID=simCHAI3D.addConstraintPlane(int deviceIndex,float[3] position,float[3] normal,float Kp,float Kv,float Fmax)"""
        ...

    def addConstraintPoint(self, deviceIndex: int, position: Any, Kp: float, Kv: float, Fmax: float) -> int:
        """int objectID=simCHAI3D.addConstraintPoint(int deviceIndex,float[3] position,float Kp,float Kv,float Fmax)"""
        ...

    def addConstraintSegment(self, deviceIndex: int, point: Any, segment: Any, Kp: float, Kv: float, Fmax: float) -> int:
        """int objectID=simCHAI3D.addConstraintSegment(int deviceIndex,float[3] point,float[3] segment,float Kp,float Kv,float Fmax)"""
        ...

    def addShape(self, vertices: list, indices: list, position: Any, orientation: Any, stiffnessFactor: float) -> int:
        """int objectID=simCHAI3D.addShape(float[] vertices,int[] indices,float[3] position,float[3] orientation,float stiffnessFactor)"""
        ...

    def readButtons(self, deviceIndex: int) -> int:
        """int buttons=simCHAI3D.readButtons(int deviceIndex)"""
        ...

    def readForce(self, deviceIndex: int) -> Any:
        """float[3] force=simCHAI3D.readForce(int deviceIndex)"""
        ...

    def readPosition(self, deviceIndex: int) -> Any:
        """float[3] position=simCHAI3D.readPosition(int deviceIndex)"""
        ...

    def removeObject(self, objectID: int) -> None:
        """simCHAI3D.removeObject(int objectID)"""
        ...

    def reset(self) -> None:
        """simCHAI3D.reset()"""
        ...

    def start(self, deviceIndex: int, toolRadius: float, workspaceRadius: float) -> int:
        """int result=simCHAI3D.start(int deviceIndex,float toolRadius,float workspaceRadius)"""
        ...

    def updateConstraint(self, objectID: int, positionA: Any, positionB: Any, Kp: float, Kv: float, Fmax: float) -> None:
        """simCHAI3D.updateConstraint(int objectID,float[3] positionA,float[3] positionB,float Kp,float Kv,float Fmax)"""
        ...

    def updateShape(self, objectID: int, position: Any, orientation: Any, stiffnessFactor: float) -> None:
        """simCHAI3D.updateShape(int objectID,float[3] position,float[3] orientation,float stiffnessFactor)"""
        ...


class simCam:
    """API functions for the `simCam` module."""

    # --- Functions ---
    def grab(self, deviceIndex: int, visionSensorHandle: int) -> int:
        """int result=simCam.grab(int deviceIndex,int visionSensorHandle)"""
        ...

    def info(self, deviceIndex: int) -> str:
        """string info=simCam.info(int deviceIndex)"""
        ...

    def start(self, deviceIndex: int, resX: int, resY: int) -> Tuple[int, int, int]:
        """int result,int resX,int resY=simCam.start(int deviceIndex,int resX,int resY)"""
        ...

    def stop(self, deviceIndex: int) -> int:
        """int result=simCam.stop(int deviceIndex)"""
        ...


class simCmd:
    """API functions for the `simCmd` module."""

    # --- Functions ---
    def clearHistory(self) -> None:
        """simCmd.clearHistory()"""
        ...

    def setSelectedScript(self) -> Tuple[Any, str]:
        """simCmd.setSelectedScript(int scriptHandle, string lang="")"""
        ...

    def setVisible(self, b: bool) -> None:
        """simCmd.setVisible(bool b)"""
        ...


class simConvex:
    """API functions for the `simConvex` module."""

    # --- Functions ---
    # Could not generate stub for: simConvex.hacd
    # Original signature: int[] convexShapeHandles = simConvex.hacd(int shapeHandle, map params = nil)

    # Could not generate stub for: simConvex.hull
    # Original signature: int convexShapeHandle = simConvex.hull(int[] objectHandles, float growth = 0.0)

    # Could not generate stub for: simConvex.qhull
    # Original signature: float[] vertices, int[] indices = simConvex.qhull(float[] points, float growth = 0.0)

    # Could not generate stub for: simConvex.vhacd
    # Original signature: int[] convexShapeHandles = simConvex.vhacd(int shapeHandle, map params = nil)


class simEigen:
    """API functions for the `simEigen` module."""

    # --- Constants ---
    op_abs: int
    op_acos: int
    op_add: int
    op_asin: int
    op_atan: int
    op_ceil: int
    op_cos: int
    op_deg: int
    op_div: int
    op_exp: int
    op_floor: int
    op_intdiv: int
    op_log: int
    op_log10: int
    op_log2: int
    op_max: int
    op_min: int
    op_mod: int
    op_rad: int
    op_sin: int
    op_sqrt: int
    op_sub: int
    op_tan: int
    op_times: int
    op_unm: int
    pluginHandle: int

    # --- Functions ---
    def Matrix(self, rows: int, cols: int, data: list) -> dict:
        """map m = simEigen.Matrix(int rows, int cols, float[] data)"""
        ...

    def Matrix:abs(self) -> dict:
        """map m = simEigen.Matrix:abs()"""
        ...

    def Matrix:acos(self) -> dict:
        """map m = simEigen.Matrix:acos()"""
        ...

    def Matrix:add(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:add(map m2)"""
        ...

    def Matrix:asin(self) -> dict:
        """map m = simEigen.Matrix:asin()"""
        ...

    def Matrix:atan(self) -> dict:
        """map m = simEigen.Matrix:atan()"""
        ...

    def Matrix:block(self, i: int, j: int, p: int, q: int) -> dict:
        """map m = simEigen.Matrix:block(int i, int j, int p, int q)"""
        ...

    def Matrix:blockassign(self, m: dict, i: int, j: int, p: int, q: int) -> dict:
        """map self = simEigen.Matrix:blockassign(map m, int i, int j, int p, int q)"""
        ...

    def Matrix:ceil(self) -> dict:
        """map m = simEigen.Matrix:ceil()"""
        ...

    def Matrix:col(self, j: int) -> dict:
        """map m = simEigen.Matrix:col(int j)"""
        ...

    def Matrix:coldata(self, j: int) -> list:
        """float[] a = simEigen.Matrix:coldata(int j)"""
        ...

    def Matrix:cols(self) -> int:
        """int number = simEigen.Matrix:cols()"""
        ...

    def Matrix:copy(self) -> dict:
        """map m = simEigen.Matrix:copy()"""
        ...

    def Matrix:cos(self) -> dict:
        """map m = simEigen.Matrix:cos()"""
        ...

    def Matrix:count(self) -> int:
        """int number = simEigen.Matrix:count()"""
        ...

    def Matrix:cross(self, v2: dict) -> dict:
        """map v = simEigen.Matrix:cross(map v2)"""
        ...

    def Matrix:data(self) -> list:
        """float[] a = simEigen.Matrix:data()"""
        ...

    def Matrix:deg(self) -> dict:
        """map m = simEigen.Matrix:deg()"""
        ...

    def Matrix:det(self) -> float:
        """float d = simEigen.Matrix:det()"""
        ...

    def Matrix:div(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:div(map m2)"""
        ...

    def Matrix:dot(self, v2: dict) -> float:
        """float the = simEigen.Matrix:dot(map v2)"""
        ...

    def Matrix:exp(self) -> dict:
        """map m = simEigen.Matrix:exp()"""
        ...

    def Matrix:eye(self, n: int) -> dict:
        """map m = simEigen.Matrix:eye(int n)"""
        ...

    def Matrix:floor(self) -> dict:
        """map m = simEigen.Matrix:floor()"""
        ...

    def Matrix:horzcat(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:horzcat(map m2)"""
        ...

    def Matrix:iabs(self) -> dict:
        """map self = simEigen.Matrix:iabs()"""
        ...

    def Matrix:iacos(self) -> dict:
        """map self = simEigen.Matrix:iacos()"""
        ...

    def Matrix:iadd(self, m: dict) -> dict:
        """map self = simEigen.Matrix:iadd(map m)"""
        ...

    def Matrix:iasin(self) -> dict:
        """map self = simEigen.Matrix:iasin()"""
        ...

    def Matrix:iatan(self) -> dict:
        """map self = simEigen.Matrix:iatan()"""
        ...

    def Matrix:iceil(self) -> dict:
        """map self = simEigen.Matrix:iceil()"""
        ...

    def Matrix:icos(self) -> dict:
        """map self = simEigen.Matrix:icos()"""
        ...

    def Matrix:ideg(self) -> dict:
        """map self = simEigen.Matrix:ideg()"""
        ...

    def Matrix:idiv(self, m: dict) -> dict:
        """map self = simEigen.Matrix:idiv(map m)"""
        ...

    def Matrix:iexp(self) -> dict:
        """map self = simEigen.Matrix:iexp()"""
        ...

    def Matrix:ifloor(self) -> dict:
        """map self = simEigen.Matrix:ifloor()"""
        ...

    def Matrix:iintdiv(self, m: dict) -> dict:
        """map self = simEigen.Matrix:iintdiv(map m)"""
        ...

    def Matrix:ilog(self) -> dict:
        """map self = simEigen.Matrix:ilog()"""
        ...

    def Matrix:ilog10(self) -> dict:
        """map self = simEigen.Matrix:ilog10()"""
        ...

    def Matrix:ilog2(self) -> dict:
        """map self = simEigen.Matrix:ilog2()"""
        ...

    def Matrix:imax(self, m: dict) -> dict:
        """map self = simEigen.Matrix:imax(map m)"""
        ...

    def Matrix:imin(self, m: dict) -> dict:
        """map self = simEigen.Matrix:imin(map m)"""
        ...

    def Matrix:imod(self, m: dict) -> dict:
        """map self = simEigen.Matrix:imod(map m)"""
        ...

    def Matrix:imul(self, m: dict) -> dict:
        """map self = simEigen.Matrix:imul(map m)"""
        ...

    def Matrix:intdiv(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:intdiv(map m2)"""
        ...

    def Matrix:inversetransform(self) -> dict:
        """map m = simEigen.Matrix:inversetransform()"""
        ...

    def Matrix:irad(self) -> dict:
        """map self = simEigen.Matrix:irad()"""
        ...

    def Matrix:isin(self) -> dict:
        """map self = simEigen.Matrix:isin()"""
        ...

    def Matrix:ismatrix(self, m: Any) -> bool:
        """bool true = simEigen.Matrix:ismatrix(any m)"""
        ...

    def Matrix:isorthogonal(self, tol: float = 1e-6) -> bool:
        """bool true = simEigen.Matrix:isorthogonal(float tol=1e-6)"""
        ...

    def Matrix:isqrt(self) -> dict:
        """map self = simEigen.Matrix:isqrt()"""
        ...

    def Matrix:isub(self, m: dict) -> dict:
        """map self = simEigen.Matrix:isub(map m)"""
        ...

    def Matrix:isvector(self, m: Any) -> bool:
        """bool true = simEigen.Matrix:isvector(any m)"""
        ...

    def Matrix:itan(self) -> dict:
        """map self = simEigen.Matrix:itan()"""
        ...

    def Matrix:item(self, i: int, j: int) -> float:
        """float value = simEigen.Matrix:item(int i, int j)"""
        ...

    def Matrix:itimes(self, m: dict) -> dict:
        """map self = simEigen.Matrix:itimes(map m)"""
        ...

    def Matrix:kron(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:kron(map m2)"""
        ...

    def Matrix:linspace(self, low: float, high: float, count: int) -> dict:
        """map m = simEigen.Matrix:linspace(float low, float high, int count)"""
        ...

    def Matrix:log(self) -> dict:
        """map m = simEigen.Matrix:log()"""
        ...

    def Matrix:log10(self) -> dict:
        """map m = simEigen.Matrix:log10()"""
        ...

    def Matrix:log2(self) -> dict:
        """map m = simEigen.Matrix:log2()"""
        ...

    def Matrix:max(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:max(map m2)"""
        ...

    def Matrix:maxcoeff(self) -> float:
        """float result = simEigen.Matrix:maxcoeff()"""
        ...

    def Matrix:min(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:min(map m2)"""
        ...

    def Matrix:mod(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:mod(map m2)"""
        ...

    def Matrix:mul(self) -> dict:
        """map m = simEigen.Matrix:mul()"""
        ...

    def Matrix:norm(self) -> float:
        """float result = simEigen.Matrix:norm()"""
        ...

    def Matrix:normalize(self) -> dict:
        """map self = simEigen.Matrix:normalize()"""
        ...

    def Matrix:normalized(self) -> dict:
        """map m = simEigen.Matrix:normalized()"""
        ...

    def Matrix:pinv(self, b: dict, damping: float) -> Tuple[dict, dict]:
        """map m, map the = simEigen.Matrix:pinv(map b, float damping)"""
        ...

    def Matrix:print(self) -> None:
        """simEigen.Matrix:print()"""
        ...

    def Matrix:prod(self) -> float:
        """float damping = simEigen.Matrix:prod()"""
        ...

    def Matrix:rad(self) -> dict:
        """map m = simEigen.Matrix:rad()"""
        ...

    def Matrix:reshaped(self, rows: int, cols: int) -> dict:
        """map m = simEigen.Matrix:reshaped(int rows, int cols)"""
        ...

    def Matrix:row(self, i: int) -> dict:
        """map m = simEigen.Matrix:row(int i)"""
        ...

    def Matrix:rowdata(self, i: int) -> list:
        """float[] a = simEigen.Matrix:rowdata(int i)"""
        ...

    def Matrix:rows(self) -> int:
        """int number = simEigen.Matrix:rows()"""
        ...

    def Matrix:setcol(self, j: int, col: dict) -> dict:
        """map self = simEigen.Matrix:setcol(int j, map col)"""
        ...

    def Matrix:setcoldata(self, j: int, data: list) -> dict:
        """map self = simEigen.Matrix:setcoldata(int j, float[] data)"""
        ...

    def Matrix:setdata(self, data: list) -> dict:
        """map self = simEigen.Matrix:setdata(float[] data)"""
        ...

    def Matrix:setitem(self, i: int, j: int, data: list) -> dict:
        """map self = simEigen.Matrix:setitem(int i, int j, float[] data)"""
        ...

    def Matrix:setrow(self, i: int, row: dict) -> dict:
        """map m = simEigen.Matrix:setrow(int i, map row)"""
        ...

    def Matrix:setrowdata(self, i: int, data: list) -> dict:
        """map self = simEigen.Matrix:setrowdata(int i, float[] data)"""
        ...

    def Matrix:sin(self) -> dict:
        """map m = simEigen.Matrix:sin()"""
        ...

    def Matrix:sqrt(self) -> dict:
        """map m = simEigen.Matrix:sqrt()"""
        ...

    def Matrix:sub(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:sub(map m2)"""
        ...

    def Matrix:svd(self, computeThinU: bool = false, computeThinV: bool = false, b: dict = nil) -> Tuple[dict, dict, dict, dict]:
        """map s, map u, map v, map x = simEigen.Matrix:svd(bool computeThinU=false, bool computeThinV=false, map b=nil)"""
        ...

    def Matrix:tan(self) -> dict:
        """map m = simEigen.Matrix:tan()"""
        ...

    def Matrix:times(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:times(map m2)"""
        ...

    def Matrix:trace(self) -> float:
        """float trace = simEigen.Matrix:trace()"""
        ...

    def Matrix:transform(self, v: dict) -> dict:
        """map m = simEigen.Matrix:transform(map v)"""
        ...

    def Matrix:transpose(self) -> dict:
        """map self = simEigen.Matrix:transpose()"""
        ...

    def Matrix:transposed(self) -> dict:
        """map m = simEigen.Matrix:transposed()"""
        ...

    def Matrix:vertcat(self, m2: dict) -> dict:
        """map m = simEigen.Matrix:vertcat(map m2)"""
        ...

    def Pose(self, t: dict, q: dict) -> dict:
        """map p = simEigen.Pose(map t, map q)"""
        ...

    def Pose:data(self) -> list:
        """float[] data = simEigen.Pose:data()"""
        ...

    def Pose:fromtransform(self, m: dict) -> dict:
        """map p = simEigen.Pose:fromtransform(map m)"""
        ...

    def Pose:inv(self) -> dict:
        """map result = simEigen.Pose:inv()"""
        ...

    def Pose:ispose(self, m: Any) -> bool:
        """bool true = simEigen.Pose:ispose(any m)"""
        ...

    def Pose:mul(self, o: dict) -> dict:
        """map p = simEigen.Pose:mul(map o)"""
        ...

    def Pose:totransform(self) -> dict:
        """map m = simEigen.Pose:totransform()"""
        ...

    def Quaternion(self, data: list = ...) -> dict:
        """map q = simEigen.Quaternion(float[] data={})"""
        ...

    def Quaternion:data(self) -> list:
        """float[] data = simEigen.Quaternion:data()"""
        ...

    def Quaternion:fromaxisangle(self, axis: dict, angle: float) -> dict:
        """map q = simEigen.Quaternion:fromaxisangle(map axis, float angle)"""
        ...

    def Quaternion:fromeuler(self, euler: dict) -> dict:
        """map q = simEigen.Quaternion:fromeuler(map euler)"""
        ...

    def Quaternion:fromrotation(self, r: dict) -> dict:
        """map q = simEigen.Quaternion:fromrotation(map r)"""
        ...

    def Quaternion:imul(self, o: dict) -> dict:
        """map self = simEigen.Quaternion:imul(map o)"""
        ...

    def Quaternion:inv(self) -> dict:
        """map result = simEigen.Quaternion:inv()"""
        ...

    def Quaternion:isquaternion(self, m: Any) -> bool:
        """bool true = simEigen.Quaternion:isquaternion(any m)"""
        ...

    def Quaternion:mul(self, o: dict) -> dict:
        """map q = simEigen.Quaternion:mul(map o)"""
        ...

    def Quaternion:slerp(self, t: float, q2: dict) -> dict:
        """map q = simEigen.Quaternion:slerp(float t, map q2)"""
        ...

    def Quaternion:toaxisangle(self) -> Tuple[dict, float]:
        """map axis, float angle = simEigen.Quaternion:toaxisangle()"""
        ...

    def Quaternion:toeuler(self) -> dict:
        """map euler = simEigen.Quaternion:toeuler()"""
        ...

    def Quaternion:torotation(self) -> dict:
        """map q = simEigen.Quaternion:torotation()"""
        ...

    def Vector(self, size: int, data: list) -> dict:
        """map v = simEigen.Vector(int size, float[] data)"""
        ...

    def mtxBlock(self, handle: str, i: int = 0, j: int = 0, p: int = -1, q: int = -1) -> str:
        """string handle = simEigen.mtxBlock(string handle, int i=0, int j=0, int p=-1, int q=-1)"""
        ...

    def mtxBlockAssign(self) -> Tuple[Any, str, int]:
        """simEigen.mtxBlockAssign(string handle, string handle2, int i=0, int j=0, int p=-1, int q=-1)"""
        ...

    def mtxCopy(self, handle: str) -> str:
        """string handle = simEigen.mtxCopy(string handle)"""
        ...

    def mtxCross(self, handle: str, handle2: str) -> str:
        """string handle = simEigen.mtxCross(string handle, string handle2)"""
        ...

    def mtxDestroy(self, handle: str) -> None:
        """simEigen.mtxDestroy(string handle)"""
        ...

    def mtxDeterminant(self, handle: str) -> float:
        """float result = simEigen.mtxDeterminant(string handle)"""
        ...

    def mtxDot(self, handle: str, handle2: str) -> float:
        """float result = simEigen.mtxDot(string handle, string handle2)"""
        ...

    def mtxGetColData(self, handle: str, j: int) -> list:
        """float[] data = simEigen.mtxGetColData(string handle, int j)"""
        ...

    def mtxGetData(self, handle: str) -> list:
        """float[] data = simEigen.mtxGetData(string handle)"""
        ...

    def mtxGetItem(self, handle: str, i: int, j: int) -> float:
        """float data = simEigen.mtxGetItem(string handle, int i, int j)"""
        ...

    def mtxGetRowData(self, handle: str, i: int) -> list:
        """float[] data = simEigen.mtxGetRowData(string handle, int i)"""
        ...

    def mtxGetSize(self, handle: str) -> Tuple[int, int]:
        """int rows, int cols = simEigen.mtxGetSize(string handle)"""
        ...

    def mtxHorzCat(self, handles: list) -> str:
        """string handle = simEigen.mtxHorzCat(string[] handles)"""
        ...

    def mtxIMul(self, handle: str, handle2: str) -> None:
        """simEigen.mtxIMul(string handle, string handle2)"""
        ...

    def mtxKron(self, handle: str, handle2: str) -> str:
        """string handle = simEigen.mtxKron(string handle, string handle2)"""
        ...

    def mtxLinSpaced(self, count: int, low: float = 1, high: float = nil) -> str:
        """string handle = simEigen.mtxLinSpaced(int count, float low=1, float high=nil)"""
        ...

    def mtxMaxCoeff(self, handle: str) -> float:
        """float result = simEigen.mtxMaxCoeff(string handle)"""
        ...

    def mtxMean(self, handle: str) -> float:
        """float result = simEigen.mtxMean(string handle)"""
        ...

    def mtxMinCoeff(self, handle: str) -> float:
        """float result = simEigen.mtxMinCoeff(string handle)"""
        ...

    def mtxMul(self, handle: str, handle2: str) -> str:
        """string handle = simEigen.mtxMul(string handle, string handle2)"""
        ...

    def mtxNew(self, rows: int, cols: int, initialData: list = ...) -> str:
        """string handle = simEigen.mtxNew(int rows, int cols, float[] initialData={})"""
        ...

    def mtxNorm(self, handle: str) -> float:
        """float result = simEigen.mtxNorm(string handle)"""
        ...

    def mtxNormalize(self, handle: str) -> None:
        """simEigen.mtxNormalize(string handle)"""
        ...

    def mtxNormalized(self, handle: str) -> str:
        """string handle = simEigen.mtxNormalized(string handle)"""
        ...

    def mtxOp(self, handle: str, op: int, handle2: str = nil, inplace: bool = true) -> str:
        """string handle = simEigen.mtxOp(string handle, int op, string handle2=nil, bool inplace=true)"""
        ...

    def mtxOpK(self, handle: str, op: int, k: float, inplace: bool = true) -> str:
        """string handle = simEigen.mtxOpK(string handle, int op, float k, bool inplace=true)"""
        ...

    def mtxPInv(self, m: str, b: str = nil, damping: float = 0) -> Tuple[str, str]:
        """string m, string x = simEigen.mtxPInv(string m, string b=nil, float damping=0)"""
        ...

    def mtxProd(self, handle: str) -> float:
        """float result = simEigen.mtxProd(string handle)"""
        ...

    def mtxReshaped(self, handle: str, rows: int, cols: int) -> str:
        """string handle = simEigen.mtxReshaped(string handle, int rows, int cols)"""
        ...

    def mtxSVD(self, m: str, computeThinU: bool = true, computeThinV: bool = true, b: str = nil) -> Tuple[str, str, str, str]:
        """string s, string u, string v, string x = simEigen.mtxSVD(string m, bool computeThinU=true, bool computeThinV=true, string b=nil)"""
        ...

    def mtxSetColData(self, handle: str, j: int, data: list) -> None:
        """simEigen.mtxSetColData(string handle, int j, float[] data)"""
        ...

    def mtxSetData(self, handle: str, data: list) -> None:
        """simEigen.mtxSetData(string handle, float[] data)"""
        ...

    def mtxSetItem(self, handle: str, i: int, j: int, data: float) -> None:
        """simEigen.mtxSetItem(string handle, int i, int j, float data)"""
        ...

    def mtxSetRowData(self, handle: str, i: int, data: list) -> None:
        """simEigen.mtxSetRowData(string handle, int i, float[] data)"""
        ...

    def mtxSquaredNorm(self, handle: str) -> float:
        """float result = simEigen.mtxSquaredNorm(string handle)"""
        ...

    def mtxSum(self, handle: str) -> float:
        """float result = simEigen.mtxSum(string handle)"""
        ...

    def mtxTrace(self, handle: str) -> float:
        """float result = simEigen.mtxTrace(string handle)"""
        ...

    def mtxTranspose(self, handle: str) -> None:
        """simEigen.mtxTranspose(string handle)"""
        ...

    def mtxTransposed(self, handle: str) -> str:
        """string handle = simEigen.mtxTransposed(string handle)"""
        ...

    def mtxVertCat(self, handles: list) -> str:
        """string handle = simEigen.mtxVertCat(string[] handles)"""
        ...

    def pinv(self, m: Any, b: Any = nil, damping: float = 0) -> Tuple[Any, Any]:
        """grid m, grid x = simEigen.pinv(grid m, grid b=nil, float damping=0)"""
        ...

    def quatDestroy(self, handle: str) -> None:
        """simEigen.quatDestroy(string handle)"""
        ...

    def quatFromAxisAngle(self, axisHandle: str, angle: float) -> str:
        """string handle = simEigen.quatFromAxisAngle(string axisHandle, float angle)"""
        ...

    def quatFromEuler(self, handle: str) -> str:
        """string handle = simEigen.quatFromEuler(string handle)"""
        ...

    def quatFromRotation(self, handle: str) -> str:
        """string handle = simEigen.quatFromRotation(string handle)"""
        ...

    def quatGetData(self, handle: str) -> Any:
        """float[4] data = simEigen.quatGetData(string handle)"""
        ...

    def quatInv(self, handle: str) -> str:
        """string handle = simEigen.quatInv(string handle)"""
        ...

    def quatMulQuat(self, handle: str, handle2: str, inplace: bool = true) -> str:
        """string handle = simEigen.quatMulQuat(string handle, string handle2, bool inplace=true)"""
        ...

    def quatMulVec(self, handle: str, vectorHandle: str) -> str:
        """string handle = simEigen.quatMulVec(string handle, string vectorHandle)"""
        ...

    def quatNew(self, initialData: Any = ..., arg1: Any, arg2: Any, arg3: Any) -> str:
        """string handle = simEigen.quatNew(float[4] initialData={0,0,0,1})"""
        ...

    def quatSLERP(self, handle: str, handle2: str, t: float) -> str:
        """string handle = simEigen.quatSLERP(string handle, string handle2, float t)"""
        ...

    def quatSetData(self, handle: str, data: Any) -> None:
        """simEigen.quatSetData(string handle, float[4] data)"""
        ...

    def quatToAxisAngle(self, handle: str) -> Tuple[str, float]:
        """string axisHandle, float angle = simEigen.quatToAxisAngle(string handle)"""
        ...

    def quatToEuler(self, handle: str) -> str:
        """string handle = simEigen.quatToEuler(string handle)"""
        ...

    def quatToRotation(self, handle: str) -> str:
        """string handle = simEigen.quatToRotation(string handle)"""
        ...

    def svd(self, m: Any, computeThinU: bool = true, computeThinV: bool = true, b: Any = nil) -> Tuple[Any, Any, Any, Any]:
        """grid s, grid u, grid v, grid x = simEigen.svd(grid m, bool computeThinU=true, bool computeThinV=true, grid b=nil)"""
        ...


class simEvents:
    """API functions for the `simEvents` module."""

    # --- Functions ---
    def addChildrenMonitor(self, callback: str, parentHandle: int) -> str:
        """string probeHandle = simEvents.addChildrenMonitor(string callback, int parentHandle)"""
        ...

    def addProbe(self, callback: str, condition: Any) -> str:
        """string probeHandle = simEvents.addProbe(string callback, any condition)"""
        ...

    def removeProbe(self, probeHandle: str) -> None:
        """simEvents.removeProbe(string probeHandle)"""
        ...


class simGLTF:
    """API functions for the `simGLTF` module."""

    # --- Constants ---
    TextureFormat_bmp: int
    TextureFormat_jpg: int
    TextureFormat_png: int
    pluginHandle: int

    # --- Functions ---
    def animationFrameCount(self) -> int:
        """int count = simGLTF.animationFrameCount()"""
        ...

    def clear(self) -> None:
        """simGLTF.clear()"""
        ...

    def exportAllObjects(self) -> None:
        """simGLTF.exportAllObjects()"""
        ...

    def exportAnimation(self) -> None:
        """simGLTF.exportAnimation()"""
        ...

    def exportObject(self, objectHandle: int) -> int:
        """int nodeIndex = simGLTF.exportObject(int objectHandle)"""
        ...

    def exportObjects(self, objectHandles: list) -> None:
        """simGLTF.exportObjects(int[] objectHandles)"""
        ...

    def exportSelectedObjects(self) -> None:
        """simGLTF.exportSelectedObjects()"""
        ...

    def exportShape(self, shapeHandle: int, parentHandle: int = -1, parentNodeIndex: int = 0) -> int:
        """int nodeIndex = simGLTF.exportShape(int shapeHandle, int parentHandle=-1, int parentNodeIndex=0)"""
        ...

    def getExportTextureFormat(self) -> Tuple[int, str]:
        """int textureFormat, string formatName = simGLTF.getExportTextureFormat()"""
        ...

    def loadASCII(self, filepath: str) -> Tuple[bool, str, str]:
        """bool result, string warnings, string errors = simGLTF.loadASCII(string filepath)"""
        ...

    def loadBinary(self, filepath: str) -> Tuple[bool, str, str]:
        """bool result, string warnings, string errors = simGLTF.loadBinary(string filepath)"""
        ...

    def recordAnimation(self, enable: bool) -> None:
        """simGLTF.recordAnimation(bool enable)"""
        ...

    def saveASCII(self, filepath: str) -> bool:
        """bool result = simGLTF.saveASCII(string filepath)"""
        ...

    def saveBinary(self, filepath: str) -> bool:
        """bool result = simGLTF.saveBinary(string filepath)"""
        ...

    def serialize(self) -> str:
        """string json = simGLTF.serialize()"""
        ...

    def setExportTextureFormat(self, textureFormat: int) -> None:
        """simGLTF.setExportTextureFormat(int textureFormat)"""
        ...


class simGeom:
    """API functions for the `simGeom` module."""

    # --- Functions ---
    def copyMesh(self, meshHandle: int) -> int:
        """int meshHandle = simGeom.copyMesh(int meshHandle)"""
        ...

    def copyOctree(self, octreeHandle: int) -> int:
        """int octreeHandle = simGeom.copyOctree(int octreeHandle)"""
        ...

    def copyPtcloud(self, ptcloudHandle: int) -> int:
        """int ptcloudHandle = simGeom.copyPtcloud(int ptcloudHandle)"""
        ...

    def createMesh(self, vertices: list, indices: list, meshOriginPos: Any = nil, meshOriginQuaternion: Any = nil, maxTriangleEdgeLength: float = 0.3, maxTriangleCountInLeafObb: int = 8) -> int:
        """int meshHandle = simGeom.createMesh(float[] vertices, int[] indices, float[3] meshOriginPos=nil, float[4] meshOriginQuaternion=nil, float maxTriangleEdgeLength=0.3, int maxTriangleCountInLeafObb=8)"""
        ...

    def createMeshFromSerializationData(self, data: str) -> int:
        """int meshHandle = simGeom.createMeshFromSerializationData(string data)"""
        ...

    def createOctreeFromColorPoints(self, points: list, octreeOriginPos: Any = nil, octreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, colors: list = nil, userData: list = nil) -> int:
        """int octreeHandle = simGeom.createOctreeFromColorPoints(float[] points, float[3] octreeOriginPos=nil, float[4] octreeOriginQuaternion=nil, float maxCellSize=0.05, float[] colors=nil, int[] userData=nil)"""
        ...

    def createOctreeFromMesh(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, octreeOriginPos: Any = nil, octreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, pointColor: Any = ..., arg7: Any, arg8: Any, userData: int = 0) -> int:
        """int octreeHandle = simGeom.createOctreeFromMesh(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] octreeOriginPos=nil, float[4] octreeOriginQuaternion=nil, float maxCellSize=0.05, int[3] pointColor={0, 0, 0}, int userData=0)"""
        ...

    def createOctreeFromOctree(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, newOctreeOriginPos: Any = nil, newOctreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, pointColor: Any = ..., arg7: Any, arg8: Any, userData: int = 0) -> int:
        """int octreeHandle = simGeom.createOctreeFromOctree(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] newOctreeOriginPos=nil, float[4] newOctreeOriginQuaternion=nil, float maxCellSize=0.05, int[3] pointColor={0, 0, 0}, int userData=0)"""
        ...

    def createOctreeFromPoints(self, points: list, octreeOriginPos: Any = nil, octreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, pointColor: Any = ..., arg5: Any, arg6: Any, userData: int = 0) -> int:
        """int octreeHandle = simGeom.createOctreeFromPoints(float[] points, float[3] octreeOriginPos=nil, float[4] octreeOriginQuaternion=nil, float maxCellSize=0.05, int[3] pointColor={0, 0, 0}, int userData=0)"""
        ...

    def createOctreeFromSerializationData(self, data: str) -> int:
        """int octreeHandle = simGeom.createOctreeFromSerializationData(string data)"""
        ...

    def createPtcloudFromColorPoints(self, points: list, octreeOriginPos: Any = nil, octreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, maxPtsInCell: int = 20, colors: list = nil, proximityTolerance: float = 0.005) -> int:
        """int ptcloudHandle = simGeom.createPtcloudFromColorPoints(float[] points, float[3] octreeOriginPos=nil, float[4] octreeOriginQuaternion=nil, float maxCellSize=0.05, int maxPtsInCell=20, float[] colors=nil, float proximityTolerance=0.005)"""
        ...

    def createPtcloudFromPoints(self, points: list, octreeOriginPos: Any = nil, octreeOriginQuaternion: Any = nil, maxCellSize: float = 0.05, maxPtsInCell: int = 20, pointColor: Any = ..., arg6: Any, arg7: Any, proximityTolerance: float = 0.005) -> int:
        """int ptcloudHandle = simGeom.createPtcloudFromPoints(float[] points, float[3] octreeOriginPos=nil, float[4] octreeOriginQuaternion=nil, float maxCellSize=0.05, int maxPtsInCell=20, int[3] pointColor={0, 0, 0}, float proximityTolerance=0.005)"""
        ...

    def createPtcloudFromSerializationData(self, data: str) -> int:
        """int ptcloudHandle = simGeom.createPtcloudFromSerializationData(string data)"""
        ...

    def destroyMesh(self, meshHandle: int) -> None:
        """simGeom.destroyMesh(int meshHandle)"""
        ...

    def destroyOctree(self, octreeHandle: int) -> None:
        """simGeom.destroyOctree(int octreeHandle)"""
        ...

    def destroyPtcloud(self, ptcloudHandle: int) -> None:
        """simGeom.destroyPtcloud(int ptcloudHandle)"""
        ...

    def getBoxBoxDistance(self, box1Pos: Any, box1Quaternion: Any, box1HalfSize: Any, box2Pos: Any, box2Quaternion: Any, box2HalfSize: Any, boxesAreSolid: bool) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getBoxBoxDistance(float[3] box1Pos, float[4] box1Quaternion, float[3] box1HalfSize, float[3] box2Pos, float[4] box2Quaternion, float[3] box2HalfSize, bool boxesAreSolid)"""
        ...

    def getBoxPointDistance(self, boxPos: Any, boxQuaternion: Any, boxHalfSize: Any, boxIsSolid: bool, point: Any) -> Tuple[float, Any]:
        """float dist, float[3] distSegPt = simGeom.getBoxPointDistance(float[3] boxPos, float[4] boxQuaternion, float[3] boxHalfSize, bool boxIsSolid, float[3] point)"""
        ...

    def getBoxSegmentDistance(self, boxPos: Any, boxQuaternion: Any, boxHalfSize: Any, boxIsSolid: bool, segmentPt1: Any, segmentPt2: Any, altRoutine: bool = false) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getBoxSegmentDistance(float[3] boxPos, float[4] boxQuaternion, float[3] boxHalfSize, bool boxIsSolid, float[3] segmentPt1, float[3] segmentPt2, bool altRoutine=false)"""
        ...

    def getBoxTriangleDistance(self, boxPos: Any, boxQuaternion: Any, boxHalfSize: Any, boxIsSolid: bool, triPt1: Any, triPt2: Any, triPt3: Any, altRoutine: bool = false) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getBoxTriangleDistance(float[3] boxPos, float[4] boxQuaternion, float[3] boxHalfSize, bool boxIsSolid, float[3] triPt1, float[3] triPt2, float[3] triPt3, bool altRoutine=false)"""
        ...

    def getMeshMeshCollision(self, mesh1Handle: int, mesh1Pos: Any, mesh1Quaternion: Any, mesh2Handle: int, mesh2Pos: Any, mesh2Quaternion: Any, cache: Any = nil, returnIntersections: bool = false) -> Tuple[bool, Any, list]:
        """bool collision, int[2] cache, float[] intersections = simGeom.getMeshMeshCollision(int mesh1Handle, float[3] mesh1Pos, float[4] mesh1Quaternion, int mesh2Handle, float[3] mesh2Pos, float[4] mesh2Quaternion, int[2] cache=nil, bool returnIntersections=false)"""
        ...

    def getMeshMeshDistance(self, mesh1Handle: int, mesh1Pos: Any, mesh1Quaternion: Any, mesh2Handle: int, mesh2Pos: Any, mesh2Quaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getMeshMeshDistance(int mesh1Handle, float[3] mesh1Pos, float[4] mesh1Quaternion, int mesh2Handle, float[3] mesh2Pos, float[4] mesh2Quaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getMeshOctreeCollision(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, cache: Any = nil) -> Tuple[bool, Any]:
        """bool collision, int[2] cache = simGeom.getMeshOctreeCollision(int meshHandle, float[3] meshPos, float[4] meshQuaternion, int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, int[2] cache=nil)"""
        ...

    def getMeshOctreeDistance(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getMeshOctreeDistance(int meshHandle, float[3] meshPos, float[4] meshQuaternion, int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getMeshPointDistance(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, point: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, int]:
        """float dist, float[3] distSegPt, int cache = simGeom.getMeshPointDistance(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] point, float distanceThreshold=0, int cache=-1)"""
        ...

    def getMeshPtcloudDistance(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getMeshPtcloudDistance(int meshHandle, float[3] meshPos, float[4] meshQuaternion, int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getMeshSegmentCollision(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, segmentPt1: Any, segmentPt2: Any, cache: int = -1, returnIntersections: bool = false) -> Tuple[bool, int, list]:
        """bool collision, int cache, float[] intersections = simGeom.getMeshSegmentCollision(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] segmentPt1, float[3] segmentPt2, int cache=-1, bool returnIntersections=false)"""
        ...

    def getMeshSegmentDistance(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, segmentPt1: Any, segmentPt2: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getMeshSegmentDistance(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] segmentPt1, float[3] segmentPt2, float distanceThreshold=0, int cache=-1)"""
        ...

    def getMeshSerializationData(self, meshHandle: int) -> str:
        """string data = simGeom.getMeshSerializationData(int meshHandle)"""
        ...

    def getMeshTriangleCollision(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, triPt1: Any, triPt2: Any, triPt3: Any, cache: int = -1, returnIntersections: bool = false) -> Tuple[bool, int, list]:
        """bool collision, int cache, float[] intersections = simGeom.getMeshTriangleCollision(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] triPt1, float[3] triPt2, float[3] triPt3, int cache=-1, bool returnIntersections=false)"""
        ...

    def getMeshTriangleDistance(self, meshHandle: int, meshPos: Any, meshQuaternion: Any, triPt1: Any, triPt2: Any, triPt3: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getMeshTriangleDistance(int meshHandle, float[3] meshPos, float[4] meshQuaternion, float[3] triPt1, float[3] triPt2, float[3] triPt3, float distanceThreshold=0, int cache=-1)"""
        ...

    def getOctreeOctreeCollision(self, octree1Handle: int, octree1Pos: Any, octree1Quaternion: Any, octree2Handle: int, octree2Pos: Any, octree2Quaternion: Any, cache: Any = nil) -> Tuple[bool, Any]:
        """bool collision, int[2] cache = simGeom.getOctreeOctreeCollision(int octree1Handle, float[3] octree1Pos, float[4] octree1Quaternion, int octree2Handle, float[3] octree2Pos, float[4] octree2Quaternion, int[2] cache=nil)"""
        ...

    def getOctreeOctreeDistance(self, octree1Handle: int, octree1Pos: Any, octree1Quaternion: Any, octree2Handle: int, octree2Pos: Any, octree2Quaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getOctreeOctreeDistance(int octree1Handle, float[3] octree1Pos, float[4] octree1Quaternion, int octree2Handle, float[3] octree2Pos, float[4] octree2Quaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getOctreePointCollision(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, point: Any, cache: int = -1) -> Tuple[bool, int]:
        """bool collision, int cache = simGeom.getOctreePointCollision(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] point, int cache=-1)"""
        ...

    def getOctreePointDistance(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, point: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, int]:
        """float dist, float[3] distSegPt, int cache = simGeom.getOctreePointDistance(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] point, float distanceThreshold=0, int cache=-1)"""
        ...

    def getOctreePtcloudCollision(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, cache: Any = nil) -> Tuple[bool, Any]:
        """bool collision, int[2] cache = simGeom.getOctreePtcloudCollision(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, int[2] cache=nil)"""
        ...

    def getOctreePtcloudDistance(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getOctreePtcloudDistance(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getOctreeSegmentCollision(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, segPt1: Any, segPt2: Any, cache: int = -1) -> Tuple[bool, int]:
        """bool collision, int cache = simGeom.getOctreeSegmentCollision(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] segPt1, float[3] segPt2, int cache=-1)"""
        ...

    def getOctreeSegmentDistance(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, segPt1: Any, segPt2: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getOctreeSegmentDistance(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] segPt1, float[3] segPt2, float distanceThreshold=0, int cache=-1)"""
        ...

    def getOctreeSerializationData(self, octreeHandle: int) -> str:
        """string data = simGeom.getOctreeSerializationData(int octreeHandle)"""
        ...

    def getOctreeTriangleCollision(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, triPt1: Any, triPt2: Any, triPt3: Any, cache: int = -1) -> Tuple[bool, int]:
        """bool collision, int cache = simGeom.getOctreeTriangleCollision(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] triPt1, float[3] triPt2, float[3] triPt3, int cache=-1)"""
        ...

    def getOctreeTriangleDistance(self, octreeHandle: int, octreePos: Any, octreeQuaternion: Any, triPt1: Any, triPt2: Any, triPt3: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getOctreeTriangleDistance(int octreeHandle, float[3] octreePos, float[4] octreeQuaternion, float[3] triPt1, float[3] triPt2, float[3] triPt3, float distanceThreshold=0, int cache=-1)"""
        ...

    def getOctreeVoxels(self, octreeHandle: int) -> Tuple[list, list, list]:
        """float[] positions, float[] colors, int[] userData = simGeom.getOctreeVoxels(int octreeHandle)"""
        ...

    def getPtcloudPointDistance(self, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, point: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, int]:
        """float dist, float[3] distSegPt, int cache = simGeom.getPtcloudPointDistance(int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, float[3] point, float distanceThreshold=0, int cache=-1)"""
        ...

    def getPtcloudPoints(self, ptcloudHandle: int, subsetProportion: float = 1.0) -> Tuple[list, list]:
        """float[] points, float[] colors = simGeom.getPtcloudPoints(int ptcloudHandle, float subsetProportion=1.0)"""
        ...

    def getPtcloudPtcloudDistance(self, ptcloud1Handle: int, ptcloud1Pos: Any, ptcloud1Quaternion: Any, ptcloud2Handle: int, ptcloud2Pos: Any, ptcloud2Quaternion: Any, distanceThreshold: float = 0, cache: Any = nil) -> Tuple[float, Any, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int[2] cache = simGeom.getPtcloudPtcloudDistance(int ptcloud1Handle, float[3] ptcloud1Pos, float[4] ptcloud1Quaternion, int ptcloud2Handle, float[3] ptcloud2Pos, float[4] ptcloud2Quaternion, float distanceThreshold=0, int[2] cache=nil)"""
        ...

    def getPtcloudSegmentDistance(self, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, segPt1: Any, segPt2: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getPtcloudSegmentDistance(int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, float[3] segPt1, float[3] segPt2, float distanceThreshold=0, int cache=-1)"""
        ...

    def getPtcloudSerializationData(self, octreeHandle: int) -> str:
        """string data = simGeom.getPtcloudSerializationData(int octreeHandle)"""
        ...

    def getPtcloudTriangleDistance(self, ptcloudHandle: int, ptcloudPos: Any, ptcloudQuaternion: Any, triPt1: Any, triPt2: Any, triPt3: Any, distanceThreshold: float = 0, cache: int = -1) -> Tuple[float, Any, Any, int]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2, int cache = simGeom.getPtcloudTriangleDistance(int ptcloudHandle, float[3] ptcloudPos, float[4] ptcloudQuaternion, float[3] triPt1, float[3] triPt2, float[3] triPt3, float distanceThreshold=0, int cache=-1)"""
        ...

    def getSegmentPointDistance(self, segmentPt1: Any, segmentPt2: Any, point: Any) -> Tuple[float, Any]:
        """float dist, float[3] distSegPt = simGeom.getSegmentPointDistance(float[3] segmentPt1, float[3] segmentPt2, float[3] point)"""
        ...

    def getSegmentSegmentDistance(self, segment1Pt1: Any, segment1Pt2: Any, segment2Pt1: Any, segment2Pt2: Any) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getSegmentSegmentDistance(float[3] segment1Pt1, float[3] segment1Pt2, float[3] segment2Pt1, float[3] segment2Pt2)"""
        ...

    def getTransformedPoints(self, points: list, position: Any, quaternion: Any) -> list:
        """float[] transformedPoints = simGeom.getTransformedPoints(float[] points, float[3] position, float[4] quaternion)"""
        ...

    def getTrianglePointDistance(self, triPt1: Any, triPt2: Any, triPt3: Any, point: Any) -> Tuple[float, Any]:
        """float dist, float[3] distSegPt = simGeom.getTrianglePointDistance(float[3] triPt1, float[3] triPt2, float[3] triPt3, float[3] point)"""
        ...

    def getTriangleSegmentDistance(self, triPt1: Any, triPt2: Any, triPt3: Any, segmentPt1: Any, segmentPt2: Any) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getTriangleSegmentDistance(float[3] triPt1, float[3] triPt2, float[3] triPt3, float[3] segmentPt1, float[3] segmentPt2)"""
        ...

    def getTriangleTriangleDistance(self, tri1Pt1: Any, tri1Pt2: Any, tri1Pt3: Any, tri2Pt1: Any, tri2Pt2: Any, tri2Pt3: Any) -> Tuple[float, Any, Any]:
        """float dist, float[3] distSegPt1, float[3] distSegPt2 = simGeom.getTriangleTriangleDistance(float[3] tri1Pt1, float[3] tri1Pt2, float[3] tri1Pt3, float[3] tri2Pt1, float[3] tri2Pt2, float[3] tri2Pt3)"""
        ...

    def scaleMesh(self, meshHandle: int, scaleFactor: float) -> None:
        """simGeom.scaleMesh(int meshHandle, float scaleFactor)"""
        ...

    def scaleOctree(self, octreeHandle: int, scaleFactor: float) -> None:
        """simGeom.scaleOctree(int octreeHandle, float scaleFactor)"""
        ...

    def scalePtcloud(self, ptcloudHandle: int, scaleFactor: float) -> None:
        """simGeom.scalePtcloud(int ptcloudHandle, float scaleFactor)"""
        ...


class simICP:
    """API functions for the `simICP` module."""

    # --- Functions ---
    def match(self, model_handle: int, template_handle: int, outlier_treshold: float = -1) -> list:
        """float[] m = simICP.match(int model_handle, int template_handle, float outlier_treshold=-1)"""
        ...

    def matchToShape(self, model_handle: int, template_handle: int, outlier_treshold: float = -1) -> list:
        """float[] m = simICP.matchToShape(int model_handle, int template_handle, float outlier_treshold=-1)"""
        ...


class simIGL:
    """API functions for the `simIGL` module."""

    # --- Constants ---
    boolean_op_difference: int
    boolean_op_intersection: int
    boolean_op_resolve: int
    boolean_op_symmetric_difference: int
    boolean_op_union: int
    pluginHandle: int

    # --- Functions ---
    def adaptiveUpsample(self, m: dict, threshold: float) -> dict:
        """map m = simIGL.adaptiveUpsample(map m, float threshold)"""
        ...

    def barycenter(self, v: Any, f: Any) -> Any:
        """grid bc = simIGL.barycenter(grid v, grid f)"""
        ...

    def centroid(self, m: dict) -> Tuple[Any, float]:
        """float[3] c, float vol = simIGL.centroid(map m)"""
        ...

    def closestFacet(self, m: dict, points: Any, emap: Any, uec: Any, uee: Any, indices: list = ...) -> Tuple[list, list]:
        """int[] r, int[] s = simIGL.closestFacet(map m, grid points, grid emap, grid uec, grid uee, int[] indices={})"""
        ...

    def convexHull(self, points: list) -> dict:
        """map m = simIGL.convexHull(float[] points)"""
        ...

    def convexHullShape(self, handles: list) -> int:
        """int handleResult = simIGL.convexHullShape(int[] handles)"""
        ...

    def drawMesh(self, mesh: dict, opts: dict) -> dict:
        """map dwo = simIGL.drawMesh(map mesh, map opts)"""
        ...

    def exactGeodesic(self, m: dict, vs: list, fs: list, vt: list, ft: list) -> list:
        """float[] distances = simIGL.exactGeodesic(map m, int[] vs, int[] fs, int[] vt, int[] ft)"""
        ...

    def faceCentroids(self, m: dict) -> Any:
        """grid c = simIGL.faceCentroids(map m)"""
        ...

    def getMesh(self, h: int, options: dict = ...) -> dict:
        """map mesh = simIGL.getMesh(int h, map options={})"""
        ...

    def intersectWithHalfSpace(self, m: dict, pt: Any, n: Any) -> Tuple[dict, list]:
        """map m, int[] j = simIGL.intersectWithHalfSpace(map m, float[3] pt, float[3] n)"""
        ...

    def meshBoolean(self, a: dict, b: dict, op: int) -> dict:
        """map result = simIGL.meshBoolean(map a, map b, int op)"""
        ...

    def meshBooleanShape(self, handles: list, op: int) -> int:
        """int handleResult = simIGL.meshBooleanShape(int[] handles, int op)"""
        ...

    def meshOctreeIntersection(self, m: dict, oc: int) -> dict:
        """map m = simIGL.meshOctreeIntersection(map m, int oc)"""
        ...

    def pointNormalToMatrix(self, point: dict, normal: dict) -> dict:
        """map matrix = simIGL.pointNormalToMatrix(map point, map normal)"""
        ...

    def randomPointsOnMesh(self, n: int, m: dict, convertToWorldCoords: bool = false) -> Tuple[Any, Any]:
        """grid b, grid fi = simIGL.randomPointsOnMesh(int n, map m, bool convertToWorldCoords=false)"""
        ...

    def rayTest(self, origin: dict, points: dict, proximitySensorHandle: int = NIL) -> dict:
        """map resultPoints = simIGL.rayTest(map origin, map points, int proximitySensorHandle=NIL)"""
        ...

    def sweptVolume(self, m: dict, transformFunc: str, timeSteps: int, gridSize: int, isoLevel: float = 0) -> dict:
        """map m = simIGL.sweptVolume(map m, string transformFunc, int timeSteps, int gridSize, float isoLevel=0)"""
        ...

    def tetrahedralize(self, m: dict, switches: str = "") -> Tuple[int, Any, Any, Any]:
        """int result, grid tv, grid tt, grid tf = simIGL.tetrahedralize(map m, string switches="")"""
        ...

    def uniqueEdgeMap(self, f: Any) -> Tuple[Any, Any, Any, Any, Any]:
        """grid e, grid ue, grid emap, grid uec, grid uee = simIGL.uniqueEdgeMap(grid f)"""
        ...

    def upsample(self, m: dict, n: int = 1) -> dict:
        """map m = simIGL.upsample(map m, int n=1)"""
        ...

    def volume(self, m: dict) -> list:
        """float[] vol = simIGL.volume(map m)"""
        ...


class simIK:
    """API functions for the `simIK` module."""

    # --- Constants ---
    calc_cannotinvert: int
    calc_invalidcallbackdata: int
    calc_limithit: int
    calc_notperformed: int
    calc_notwithintolerance: int
    calc_stepstoobig: int
    constraint_alpha_beta: int
    constraint_gamma: int
    constraint_orientation: int
    constraint_pose: int
    constraint_position: int
    constraint_x: int
    constraint_y: int
    constraint_z: int
    group_avoidlimits: int
    group_enabled: int
    group_ignoremaxsteps: int
    group_restoreonbadangtol: int
    group_restoreonbadlintol: int
    group_stoponlimithit: int
    handle_all: int
    handle_parent: int
    handle_world: int
    handleflag_tipdummy: int
    jointmode_ik: int
    jointmode_passive: int
    jointtype_prismatic: int
    jointtype_revolute: int
    jointtype_spherical: int
    method_damped_least_squares: int
    method_jacobian_transpose: int
    method_pseudo_inverse: int
    method_undamped_pseudo_inverse: int
    objecttype_dummy: int
    objecttype_joint: int
    pluginHandle: int
    result_fail: int
    result_not_performed: int
    result_success: int

    # --- Functions ---
    def addElement(self, environmentHandle: int, ikGroupHandle: int, tipDummyHandle: int) -> int:
        """int elementHandle = simIK.addElement(int environmentHandle, int ikGroupHandle, int tipDummyHandle)"""
        ...

    def addElementFromScene(self, environmentHandle: int, ikGroup: int, baseHandle: int, tipHandle: int, targetHandle: int, constraints: int) -> Tuple[int, dict, dict]:
        """int ikElement, map simToIkMap, map ikToSimMap = simIK.addElementFromScene(int environmentHandle, int ikGroup, int baseHandle, int tipHandle, int targetHandle, int constraints)"""
        ...

    def computeGroupJacobian(self, environmentHandle: int, ikGroupHandle: int) -> Tuple[list, list]:
        """float[] jacobian, float[] errorVector = simIK.computeGroupJacobian(int environmentHandle, int ikGroupHandle)"""
        ...

    def computeJacobian(self, environmentHandle: int, baseObject: int, lastJoint: int, constraints: int, tipMatrix: Any, targetMatrix: Any = nil, constrBaseMatrix: Any = nil) -> Tuple[list, list]:
        """float[] jacobian, float[] errorVector = simIK.computeJacobian(int environmentHandle, int baseObject, int lastJoint, int constraints, float[7..12] tipMatrix, float[7..12] targetMatrix=nil, float[7..12] constrBaseMatrix=nil)"""
        ...

    def createDebugOverlay(self, environmentHandle: int, tipHandle: int, baseHandle: int = -1) -> int:
        """int debugObject = simIK.createDebugOverlay(int environmentHandle, int tipHandle, int baseHandle=-1)"""
        ...

    def createDummy(self, environmentHandle: int, dummyName: str = '') -> int:
        """int dummyHandle = simIK.createDummy(int environmentHandle, string dummyName='')"""
        ...

    def createEnvironment(self, flags: int = 0) -> int:
        """int environmentHandle = simIK.createEnvironment(int flags=0)"""
        ...

    def createGroup(self, environmentHandle: int, ikGroupName: str = '') -> int:
        """int ikGroupHandle = simIK.createGroup(int environmentHandle, string ikGroupName='')"""
        ...

    def createJoint(self, environmentHandle: int, jointType: int, jointName: str = '') -> int:
        """int jointHandle = simIK.createJoint(int environmentHandle, int jointType, string jointName='')"""
        ...

    def doesGroupExist(self, environmentHandle: int, ikGroupName: str) -> bool:
        """bool result = simIK.doesGroupExist(int environmentHandle, string ikGroupName)"""
        ...

    def doesObjectExist(self, environmentHandle: int, objectName: str) -> bool:
        """bool result = simIK.doesObjectExist(int environmentHandle, string objectName)"""
        ...

    def duplicateEnvironment(self, environmentHandle: int) -> int:
        """int duplicateEnvHandle = simIK.duplicateEnvironment(int environmentHandle)"""
        ...

    def eraseDebugOverlay(self, debugObject: int) -> None:
        """simIK.eraseDebugOverlay(int debugObject)"""
        ...

    def eraseEnvironment(self, environmentHandle: int) -> None:
        """simIK.eraseEnvironment(int environmentHandle)"""
        ...

    def eraseObject(self, environmentHandle: int, objectHandle: int) -> None:
        """simIK.eraseObject(int environmentHandle, int objectHandle)"""
        ...

    def findConfigs(self, envHandle: int, ikGroupHandle: int, jointHandles: list, params: dict = ..., configs: list = ...) -> list:
        """any[] configs = simIK.findConfigs(int envHandle, int ikGroupHandle, int[] jointHandles, map params={}, any[] configs={})"""
        ...

    def generatePath(self, environmentHandle: int, ikGroupHandle: int, jointHandles: list, tipHandle: int, pathPointCount: int, validationCallback: Any = nil, auxData: Any = nil) -> list:
        """float[] path = simIK.generatePath(int environmentHandle, int ikGroupHandle, int[] jointHandles, int tipHandle, int pathPointCount, func validationCallback=nil, any auxData=nil)"""
        ...

    def getAlternateConfigs(self, environmentHandle: int, jointHandles: list, lowLimits: list = nil, ranges: list = nil) -> list:
        """float[] configs = simIK.getAlternateConfigs(int environmentHandle, int[] jointHandles, float[] lowLimits=nil, float[] ranges=nil)"""
        ...

    def getElementBase(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int) -> Tuple[int, int]:
        """int baseHandle, int constraintsBaseHandle = simIK.getElementBase(int environmentHandle, int ikGroupHandle, int elementHandle)"""
        ...

    def getElementConstraints(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int) -> int:
        """int constraints = simIK.getElementConstraints(int environmentHandle, int ikGroupHandle, int elementHandle)"""
        ...

    def getElementFlags(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int) -> int:
        """int flags = simIK.getElementFlags(int environmentHandle, int ikGroupHandle, int elementHandle)"""
        ...

    def getElementPrecision(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int) -> Any:
        """float[2] precision = simIK.getElementPrecision(int environmentHandle, int ikGroupHandle, int elementHandle)"""
        ...

    def getElementWeights(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int) -> Any:
        """float[2] weights = simIK.getElementWeights(int environmentHandle, int ikGroupHandle, int elementHandle)"""
        ...

    def getFailureDescription(self, reason: int) -> str:
        """string description = simIK.getFailureDescription(int reason)"""
        ...

    def getGroupCalculation(self, environmentHandle: int, ikGroupHandle: int) -> Tuple[int, float, int]:
        """int method, float damping, int maxIterations = simIK.getGroupCalculation(int environmentHandle, int ikGroupHandle)"""
        ...

    def getGroupFlags(self, environmentHandle: int, ikGroupHandle: int) -> int:
        """int flags = simIK.getGroupFlags(int environmentHandle, int ikGroupHandle)"""
        ...

    def getGroupHandle(self, environmentHandle: int, ikGroupName: str) -> int:
        """int ikGroupHandle = simIK.getGroupHandle(int environmentHandle, string ikGroupName)"""
        ...

    def getGroupJointLimitHits(self, environmentHandle: int, ikGroupHandle: int) -> Tuple[list, list]:
        """int[] jointHandles, float[] underOrOvershots = simIK.getGroupJointLimitHits(int environmentHandle, int ikGroupHandle)"""
        ...

    def getGroupJoints(self, environmentHandle: int, ikGroupHandle: int) -> list:
        """int[] jointHandles = simIK.getGroupJoints(int environmentHandle, int ikGroupHandle)"""
        ...

    def getJointDependency(self, environmentHandle: int, jointHandle: int) -> Tuple[int, float, float]:
        """int depJointHandle, float offset, float mult = simIK.getJointDependency(int environmentHandle, int jointHandle)"""
        ...

    def getJointInterval(self, environmentHandle: int, jointHandle: int) -> Tuple[bool, Any]:
        """bool cyclic, float[2] interval = simIK.getJointInterval(int environmentHandle, int jointHandle)"""
        ...

    def getJointLimitMargin(self, environmentHandle: int, jointHandle: int) -> float:
        """float margin = simIK.getJointLimitMargin(int environmentHandle, int jointHandle)"""
        ...

    def getJointMatrix(self, environmentHandle: int, jointHandle: int) -> Any:
        """float[12] matrix = simIK.getJointMatrix(int environmentHandle, int jointHandle)"""
        ...

    def getJointMaxStepSize(self, environmentHandle: int, jointHandle: int) -> float:
        """float stepSize = simIK.getJointMaxStepSize(int environmentHandle, int jointHandle)"""
        ...

    def getJointMode(self, environmentHandle: int, jointHandle: int) -> int:
        """int jointMode = simIK.getJointMode(int environmentHandle, int jointHandle)"""
        ...

    def getJointPosition(self, environmentHandle: int, jointHandle: int) -> float:
        """float position = simIK.getJointPosition(int environmentHandle, int jointHandle)"""
        ...

    def getJointScrewLead(self, environmentHandle: int, jointHandle: int) -> float:
        """float lead = simIK.getJointScrewLead(int environmentHandle, int jointHandle)"""
        ...

    def getJointTransformation(self, environmentHandle: int, jointHandle: int) -> Tuple[Any, Any, Any]:
        """float[3] position, float[4] quaternion, float[3] euler = simIK.getJointTransformation(int environmentHandle, int jointHandle)"""
        ...

    def getJointType(self, environmentHandle: int, jointHandle: int) -> int:
        """int jointType = simIK.getJointType(int environmentHandle, int jointHandle)"""
        ...

    def getJointWeight(self, environmentHandle: int, jointHandle: int) -> float:
        """float weight = simIK.getJointWeight(int environmentHandle, int jointHandle)"""
        ...

    def getObjectHandle(self, environmentHandle: int, objectName: str) -> int:
        """int objectHandle = simIK.getObjectHandle(int environmentHandle, string objectName)"""
        ...

    def getObjectMatrix(self, environmentHandle: int, objectHandle: int, relativeToObjectHandle: int = simIK.handle_world) -> Any:
        """float[12] matrix = simIK.getObjectMatrix(int environmentHandle, int objectHandle, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def getObjectParent(self, environmentHandle: int, objectHandle: int) -> int:
        """int parentObjectHandle = simIK.getObjectParent(int environmentHandle, int objectHandle)"""
        ...

    def getObjectPose(self, environmentHandle: int, objectHandle: int, relativeToObjectHandle: int = simIK.handle_world) -> Any:
        """float[7] pose = simIK.getObjectPose(int environmentHandle, int objectHandle, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def getObjectTransformation(self, environmentHandle: int, objectHandle: int, relativeToObjectHandle: int = simIK.handle_world) -> Tuple[Any, Any, Any]:
        """float[3] position, float[4] quaternion, float[3] euler = simIK.getObjectTransformation(int environmentHandle, int objectHandle, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def getObjectType(self, environmentHandle: int, objectHandle: int) -> int:
        """int objectType = simIK.getObjectType(int environmentHandle, int objectHandle)"""
        ...

    def getObjects(self, environmentHandle: int, index: int) -> Tuple[int, str, bool, int]:
        """int objectHandle, string objectName, bool isJoint, int jointType = simIK.getObjects(int environmentHandle, int index)"""
        ...

    def getTargetDummy(self, environmentHandle: int, dummyHandle: int) -> int:
        """int targetDummyHandle = simIK.getTargetDummy(int environmentHandle, int dummyHandle)"""
        ...

    def handleGroup(self, environmentHandle: int, ikGroup: int, options: dict = ...) -> Tuple[int, int, Any]:
        """int success, int flags, float[2] precision = simIK.handleGroup(int environmentHandle, int ikGroup, map options={})"""
        ...

    def handleGroups(self, environmentHandle: int, ikGroups: list, options: dict = ...) -> Tuple[int, int, Any]:
        """int success, int flags, float[2] precision = simIK.handleGroups(int environmentHandle, int[] ikGroups, map options={})"""
        ...

    def load(self, environmentHandle: int, data: str) -> None:
        """simIK.load(int environmentHandle, string data)"""
        ...

    def save(self, environmentHandle: int) -> str:
        """string data = simIK.save(int environmentHandle)"""
        ...

    def setElementBase(self) -> Tuple[Any, int, int, int, int]:
        """simIK.setElementBase(int environmentHandle, int ikGroupHandle, int elementHandle, int baseHandle, int constraintsBaseHandle=-1)"""
        ...

    def setElementConstraints(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int, constraints: int) -> None:
        """simIK.setElementConstraints(int environmentHandle, int ikGroupHandle, int elementHandle, int constraints)"""
        ...

    def setElementFlags(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int, flags: int) -> None:
        """simIK.setElementFlags(int environmentHandle, int ikGroupHandle, int elementHandle, int flags)"""
        ...

    def setElementPrecision(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int, precision: Any) -> None:
        """simIK.setElementPrecision(int environmentHandle, int ikGroupHandle, int elementHandle, float[2] precision)"""
        ...

    def setElementWeights(self, environmentHandle: int, ikGroupHandle: int, elementHandle: int, weights: Any) -> None:
        """simIK.setElementWeights(int environmentHandle, int ikGroupHandle, int elementHandle, float[2] weights)"""
        ...

    def setGroupCalculation(self, environmentHandle: int, ikGroupHandle: int, method: int, damping: float, maxIterations: int) -> None:
        """simIK.setGroupCalculation(int environmentHandle, int ikGroupHandle, int method, float damping, int maxIterations)"""
        ...

    def setGroupFlags(self, environmentHandle: int, ikGroupHandle: int, flags: int) -> None:
        """simIK.setGroupFlags(int environmentHandle, int ikGroupHandle, int flags)"""
        ...

    def setJointDependency(self) -> Tuple[Any, int, int, float]:
        """simIK.setJointDependency(int environmentHandle, int jointHandle, int masterJointHandle, float offset=0.0, float mult=1.0, func callback=nil)"""
        ...

    def setJointInterval(self) -> Tuple[Any, int, bool, Any]:
        """simIK.setJointInterval(int environmentHandle, int jointHandle, bool cyclic, float[2] interval={})"""
        ...

    def setJointLimitMargin(self, environmentHandle: int, jointHandle: int, margin: float) -> None:
        """simIK.setJointLimitMargin(int environmentHandle, int jointHandle, float margin)"""
        ...

    def setJointMaxStepSize(self, environmentHandle: int, jointHandle: int, stepSize: float) -> None:
        """simIK.setJointMaxStepSize(int environmentHandle, int jointHandle, float stepSize)"""
        ...

    def setJointMode(self, environmentHandle: int, jointHandle: int, jointMode: int) -> None:
        """simIK.setJointMode(int environmentHandle, int jointHandle, int jointMode)"""
        ...

    def setJointPosition(self, environmentHandle: int, jointHandle: int, position: float) -> None:
        """simIK.setJointPosition(int environmentHandle, int jointHandle, float position)"""
        ...

    def setJointScrewLead(self, environmentHandle: int, jointHandle: int, lead: float) -> None:
        """simIK.setJointScrewLead(int environmentHandle, int jointHandle, float lead)"""
        ...

    def setJointWeight(self, environmentHandle: int, jointHandle: int, weight: float) -> None:
        """simIK.setJointWeight(int environmentHandle, int jointHandle, float weight)"""
        ...

    def setObjectMatrix(self) -> Tuple[Any, int, Any, int]:
        """simIK.setObjectMatrix(int environmentHandle, int objectHandle, float[12] matrix, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def setObjectParent(self) -> Tuple[Any, int, int, bool]:
        """simIK.setObjectParent(int environmentHandle, int objectHandle, int parentObjectHandle, bool keepInPlace=true)"""
        ...

    def setObjectPose(self) -> Tuple[Any, int, Any, int]:
        """simIK.setObjectPose(int environmentHandle, int objectHandle, float[7] pose, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def setObjectTransformation(self) -> Tuple[Any, int, Any, list, int]:
        """simIK.setObjectTransformation(int environmentHandle, int objectHandle, float[3] position, float[] eulerOrQuaternion, int relativeToObjectHandle=simIK.handle_world)"""
        ...

    def setSphericalJointMatrix(self, environmentHandle: int, jointHandle: int, matrix: Any) -> None:
        """simIK.setSphericalJointMatrix(int environmentHandle, int jointHandle, float[12] matrix)"""
        ...

    def setSphericalJointRotation(self, environmentHandle: int, jointHandle: int, eulerOrQuaternion: list) -> None:
        """simIK.setSphericalJointRotation(int environmentHandle, int jointHandle, float[] eulerOrQuaternion)"""
        ...

    def setTargetDummy(self, environmentHandle: int, dummyHandle: int, targetDummyHandle: int) -> None:
        """simIK.setTargetDummy(int environmentHandle, int dummyHandle, int targetDummyHandle)"""
        ...

    def syncFromSim(self, environmentHandle: int, ikGroups: list) -> None:
        """simIK.syncFromSim(int environmentHandle, int[] ikGroups)"""
        ...

    def syncToSim(self, environmentHandle: int, ikGroups: list) -> None:
        """simIK.syncToSim(int environmentHandle, int[] ikGroups)"""
        ...


class simIM:
    """API functions for the `simIM` module."""

    # --- Constants ---
    cmpOp_eq: int
    cmpOp_ge: int
    cmpOp_gt: int
    cmpOp_le: int
    cmpOp_lt: int
    cmpOp_ne: int
    dict_type__4X4_100: int
    dict_type__4X4_1000: int
    dict_type__4X4_250: int
    dict_type__4X4_50: int
    dict_type__5X5_100: int
    dict_type__5X5_1000: int
    dict_type__5X5_250: int
    dict_type__5X5_50: int
    dict_type__6X6_100: int
    dict_type__6X6_1000: int
    dict_type__6X6_250: int
    dict_type__6X6_50: int
    dict_type__7X7_100: int
    dict_type__7X7_1000: int
    dict_type__7X7_250: int
    dict_type__7X7_50: int
    dict_type__APRILTAG_16h5: int
    dict_type__APRILTAG_25h9: int
    dict_type__APRILTAG_36h10: int
    dict_type__APRILTAG_36h11: int
    dict_type__ARUCO_ORIGINAL: int
    dist_C: int
    dist_L1: int
    dist_L2: int
    flipOp_both: int
    flipOp_x: int
    flipOp_y: int
    fontFace_complex: int
    fontFace_complex_small: int
    fontFace_duplex: int
    fontFace_plain: int
    fontFace_script_complex: int
    fontFace_script_simplex: int
    fontFace_simplex: int
    fontFace_triplex: int
    format__32FC1: int
    format__32FC3: int
    format__32FC4: int
    format__8UC1: int
    format__8UC3: int
    format__8UC4: int
    interp_area: int
    interp_cubic: int
    interp_lanczos4: int
    interp_linear: int
    interp_nearest: int
    maskSize__3x3: int
    maskSize__5x5: int
    maskSize__precise: int
    pluginHandle: int
    reduceOp_avg: int
    reduceOp_max: int
    reduceOp_min: int
    reduceOp_sum: int

    # --- Functions ---
    def abs(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.abs(string handle, bool inPlace=false)"""
        ...

    def absdiff(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.absdiff(string handle1, string handle2, bool inPlace=false)"""
        ...

    def absdiffK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.absdiffK(string handle, float[] k, bool inPlace=false)"""
        ...

    def add(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.add(string handle1, string handle2, bool inPlace=false)"""
        ...

    def addK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.addK(string handle, float[] k, bool inPlace=false)"""
        ...

    def addWeighted(self, handle1: str, handle2: str, alpha: float, beta: float, gamma: float, inPlace: bool = false) -> str:
        """string handle = simIM.addWeighted(string handle1, string handle2, float alpha, float beta, float gamma, bool inPlace=false)"""
        ...

    def arrowedLine(self) -> Tuple[Any, Any, Any, Any, int]:
        """simIM.arrowedLine(string handle, int[2] p1, int[2] p2, int[3] color, int thickness=1, int type=8, int shift=0, float tipLength=0.1)"""
        ...

    def bitwiseAnd(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseAnd(string handle1, string handle2, bool inPlace=false)"""
        ...

    def bitwiseAndK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseAndK(string handle, float[] k, bool inPlace=false)"""
        ...

    def bitwiseNot(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseNot(string handle, bool inPlace=false)"""
        ...

    def bitwiseOr(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseOr(string handle1, string handle2, bool inPlace=false)"""
        ...

    def bitwiseOrK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseOrK(string handle, float[] k, bool inPlace=false)"""
        ...

    def bitwiseXor(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseXor(string handle1, string handle2, bool inPlace=false)"""
        ...

    def bitwiseXorK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.bitwiseXorK(string handle, float[] k, bool inPlace=false)"""
        ...

    def cart2polar(self, handle1: str, handle2: str, angleInDegrees: bool = false) -> Tuple[str, str]:
        """string handle1, string handle2 = simIM.cart2polar(string handle1, string handle2, bool angleInDegrees=false)"""
        ...

    def circle(self) -> Tuple[Any, Any, int, Any, int]:
        """simIM.circle(string handle, int[2] center, int radius, int[3] color, int thickness=1, int type=8, int shift=0)"""
        ...

    def clipLine(self, handle: str, p1: Any, p2: Any) -> Tuple[bool, Any, Any]:
        """bool valid, int[2] p1, int[2] p2 = simIM.clipLine(string handle, int[2] p1, int[2] p2)"""
        ...

    def closeVideoCapture(self, deviceIndex: int) -> None:
        """simIM.closeVideoCapture(int deviceIndex)"""
        ...

    def compare(self, handle1: str, handle2: str, op: int, inPlace: bool = false) -> str:
        """string handle = simIM.compare(string handle1, string handle2, int op, bool inPlace=false)"""
        ...

    def compareK(self, handle: str, k: list, op: int, inPlace: bool = false) -> str:
        """string handle = simIM.compareK(string handle, float[] k, int op, bool inPlace=false)"""
        ...

    def convert(self, handle: str, format: int, scale: float = 1.0, inPlace: bool = false) -> str:
        """string handle = simIM.convert(string handle, int format, float scale=1.0, bool inPlace=false)"""
        ...

    def copy(self, srcHandle: str, srcOffset: Any, dstHandle: str, dstOffset: Any, size: Any) -> None:
        """simIM.copy(string srcHandle, int[2] srcOffset, string dstHandle, int[2] dstOffset, int[2] size)"""
        ...

    def create(self, width: int, height: int, format: int = simim_fmt_8UC3, initialValue: int = 0) -> str:
        """string handle = simIM.create(int width, int height, int format=simim_fmt_8UC3, int initialValue=0)"""
        ...

    def createFromData(self, width: int, height: int, data: bytes, format: int = simim_fmt_8UC3) -> str:
        """string handle = simIM.createFromData(int width, int height, buffer data, int format=simim_fmt_8UC3)"""
        ...

    def dataURL(self, imgHandle: str, format: str = BMP) -> str:
        """string output = simIM.dataURL(string imgHandle, string format=BMP)"""
        ...

    def destroy(self, handle: str) -> None:
        """simIM.destroy(string handle)"""
        ...

    def detectMarkers(self, handle: str, dictionaryHandle: str) -> Tuple[list, list, list]:
        """float[] corners, int[] markerIds, float[] rejectedCandidates = simIM.detectMarkers(string handle, string dictionaryHandle)"""
        ...

    def distanceTransform(self, handle: str, distanceType: int = simim_dist_L2, maskSize: int = simim_masksize_precise, inPlace: bool = false) -> str:
        """string handle = simIM.distanceTransform(string handle, int distanceType=simim_dist_L2, int maskSize=simim_masksize_precise, bool inPlace=false)"""
        ...

    def divide(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.divide(string handle1, string handle2, bool inPlace=false)"""
        ...

    def divideK(self, k: list, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.divideK(float[] k, string handle, bool inPlace=false)"""
        ...

    def drawMarker(self, dictionaryHandle: str, markerId: int, size: int, handle: str = "", borderSize: int = 1) -> str:
        """string handle = simIM.drawMarker(string dictionaryHandle, int markerId, int size, string handle="", int borderSize=1)"""
        ...

    def ellipse(self) -> Tuple[Any, Any, Any, float]:
        """simIM.ellipse(string handle, int[2] center, int[2] radius, float angle=0.0, float startAngle=0.0, float endAngle=360.0, int[3] color={255,255,255}, int thickness=1, int type=8, int shift=0)"""
        ...

    def encode(self, handle: str, format: str) -> str:
        """string output = simIM.encode(string handle, string format)"""
        ...

    def exp(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.exp(string handle, bool inPlace=false)"""
        ...

    def fillConvexPoly(self) -> Tuple[Any, list, Any, int]:
        """simIM.fillConvexPoly(string handle, int[] points, int[3] color, int type=8, int shift=0)"""
        ...

    def fillPoly(self) -> Tuple[Any, list, list, Any, Any, int]:
        """simIM.fillPoly(string handle, int[] points, int[] numPoints, int[2] offset, int[3] color, int type=8, int shift=0)"""
        ...

    def flip(self, handle: str, op: int = 0, inPlace: bool = false) -> str:
        """string handle = simIM.flip(string handle, int op=0, bool inPlace=false)"""
        ...

    def get(self, handle: str, coord: Any) -> list:
        """float[] value = simIM.get(string handle, int[2] coord)"""
        ...

    def getFormat(self, handle: str) -> int:
        """int format = simIM.getFormat(string handle)"""
        ...

    def getMarkerBitSize(self, dictType: int) -> int:
        """int size = simIM.getMarkerBitSize(int dictType)"""
        ...

    def getMarkerDictionary(self, type: int) -> str:
        """string handle = simIM.getMarkerDictionary(int type)"""
        ...

    def gray2rgb(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.gray2rgb(string handle, bool inPlace=false)"""
        ...

    def hls2rgb(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.hls2rgb(string handle, bool inPlace=false)"""
        ...

    def hsv2rgb(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.hsv2rgb(string handle, bool inPlace=false)"""
        ...

    def line(self) -> Tuple[Any, Any, Any, Any, int]:
        """simIM.line(string handle, int[2] p1, int[2] p2, int[3] color, int thickness=1, int type=8, int shift=0)"""
        ...

    def log(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.log(string handle, bool inPlace=false)"""
        ...

    def magnitude(self, handle1: str, handle2: str) -> str:
        """string handle = simIM.magnitude(string handle1, string handle2)"""
        ...

    def merge(self, handles: list) -> str:
        """string handle = simIM.merge(string[] handles)"""
        ...

    def mixChannels(self, inputHandles: list, outputHandles: list, fromTo: list) -> None:
        """simIM.mixChannels(string[] inputHandles, string[] outputHandles, int[] fromTo)"""
        ...

    def multiply(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.multiply(string handle1, string handle2, bool inPlace=false)"""
        ...

    def openVideoCapture(self, deviceIndex: int) -> None:
        """simIM.openVideoCapture(int deviceIndex)"""
        ...

    def phase(self, handle1: str, handle2: str, angleInDegrees: bool = false) -> str:
        """string handle = simIM.phase(string handle1, string handle2, bool angleInDegrees=false)"""
        ...

    def polar2cart(self, handle1: str, handle2: str, angleInDegrees: bool = false) -> Tuple[str, str]:
        """string handle1, string handle2 = simIM.polar2cart(string handle1, string handle2, bool angleInDegrees=false)"""
        ...

    def polylines(self) -> Tuple[Any, list, list, bool, Any, int]:
        """simIM.polylines(string handle, int[] points, int[] numPoints, bool isClosed, int[3] color, int thickness=1, int type=8, int shift=0)"""
        ...

    def pow(self, handle: str, power: float, inPlace: bool = false) -> str:
        """string handle = simIM.pow(string handle, float power, bool inPlace=false)"""
        ...

    def read(self, filename: str) -> str:
        """string handle = simIM.read(string filename)"""
        ...

    def readFromVideoCapture(self, deviceIndex: int, handle: str = "") -> str:
        """string handle = simIM.readFromVideoCapture(int deviceIndex, string handle="")"""
        ...

    def readFromVisionSensor(self, sensorHandle: int, handle: str = "") -> str:
        """string handle = simIM.readFromVisionSensor(int sensorHandle, string handle="")"""
        ...

    def rectangle(self) -> Tuple[Any, Any, Any, Any, int]:
        """simIM.rectangle(string handle, int[2] p1, int[2] p2, int[3] color, int thickness=1, int type=8, int shift=0)"""
        ...

    def reduce(self, handle: str, dim: int, op: int, inPlace: bool = false) -> str:
        """string handle = simIM.reduce(string handle, int dim, int op, bool inPlace=false)"""
        ...

    def repeat(self, handle: str, nx: int, ny: int, inPlace: bool = false) -> str:
        """string handle = simIM.repeat(string handle, int nx, int ny, bool inPlace=false)"""
        ...

    def resize(self, handle: str, width: int, height: int, interpolation: int = simim_interp_linear, inPlace: bool = false) -> str:
        """string handle = simIM.resize(string handle, int width, int height, int interpolation=simim_interp_linear, bool inPlace=false)"""
        ...

    def rgb2gray(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.rgb2gray(string handle, bool inPlace=false)"""
        ...

    def rgb2hls(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.rgb2hls(string handle, bool inPlace=false)"""
        ...

    def rgb2hsv(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.rgb2hsv(string handle, bool inPlace=false)"""
        ...

    def scaleAdd(self, handle1: str, handle2: str, alpha: float, inPlace: bool = false) -> str:
        """string handle = simIM.scaleAdd(string handle1, string handle2, float alpha, bool inPlace=false)"""
        ...

    def set(self, handle: str, coord: Any, value: list) -> None:
        """simIM.set(string handle, int[2] coord, float[] value)"""
        ...

    def size(self, handle: str) -> Any:
        """int[2] size = simIM.size(string handle)"""
        ...

    def split(self, handle: str) -> list:
        """string[] handles = simIM.split(string handle)"""
        ...

    def sqrt(self, handle: str, inPlace: bool = false) -> str:
        """string handle = simIM.sqrt(string handle, bool inPlace=false)"""
        ...

    def subtract(self, handle1: str, handle2: str, inPlace: bool = false) -> str:
        """string handle = simIM.subtract(string handle1, string handle2, bool inPlace=false)"""
        ...

    def subtractK(self, handle: str, k: list, inPlace: bool = false) -> str:
        """string handle = simIM.subtractK(string handle, float[] k, bool inPlace=false)"""
        ...

    def text(self) -> Tuple[Any, str, Any, int]:
        """simIM.text(string handle, string str, int[2] pos, int fontFace=simim_fontface_simplex, bool italic=false, float fontScale=1.0, int[3] color={255,255,255}, int thickness=1, int type=8, bool bottomLeftOrigin=false)"""
        ...

    def textSize(self, str: str, fontFace: int = simim_fontface_simplex, italic: bool = false, fontScale: float = 1.0, thickness: int = 1) -> Tuple[int, int, int]:
        """int width, int height, int baseline = simIM.textSize(string str, int fontFace=simim_fontface_simplex, bool italic=false, float fontScale=1.0, int thickness=1)"""
        ...

    def write(self, handle: str, filename: str) -> None:
        """simIM.write(string handle, string filename)"""
        ...

    def writeToTexture(self, handle: str, textureId: int) -> None:
        """simIM.writeToTexture(string handle, int textureId)"""
        ...

    def writeToVisionSensor(self, handle: str, sensorHandle: int) -> None:
        """simIM.writeToVisionSensor(string handle, int sensorHandle)"""
        ...


class simLDraw:
    """API functions for the `simLDraw` module."""

    # --- Functions ---
    def import(self, filePath: str) -> list:
        """int[] handles = simLDraw.import(string filePath)"""
        ...


class simMIDI:
    """API functions for the `simMIDI` module."""

    # --- Functions ---
    def closeMidiIn(self, inputPortHandle: str) -> None:
        """simMIDI.closeMidiIn(string inputPortHandle)"""
        ...

    def closeMidiOut(self, outputPortHandle: str) -> None:
        """simMIDI.closeMidiOut(string outputPortHandle)"""
        ...

    def getMessage(self, inputPortHandle: str) -> list:
        """int[] messageData = simMIDI.getMessage(string inputPortHandle)"""
        ...

    def ignoreTypes(self, inputPortHandle: str, sysex: bool, timing: bool, activeSensing: bool) -> None:
        """simMIDI.ignoreTypes(string inputPortHandle, bool sysex, bool timing, bool activeSensing)"""
        ...

    def openMidiIn(self, inputPortIndex: int) -> str:
        """string inputPortHandle = simMIDI.openMidiIn(int inputPortIndex)"""
        ...

    def openMidiOut(self, outputPortIndex: int) -> str:
        """string outputPortHandle = simMIDI.openMidiOut(int outputPortIndex)"""
        ...

    def processIncomingMessages(self, midiInPortHandle: str, channels: list, funcs: dict) -> None:
        """simMIDI.processIncomingMessages(string midiInPortHandle, int[] channels, map funcs)"""
        ...

    def sendMessage(self, outputPortHandle: str, messageData: list) -> None:
        """simMIDI.sendMessage(string outputPortHandle, int[] messageData)"""
        ...


class simMTB:
    """API functions for the `simMTB` module."""

    # --- Functions ---
    def connectInput(self, inputMtbServerHandle: int, inputBitNumber: int, outputMtbServerHandle: int, outputBitNumber: int, connectionType: int) -> bool:
        """bool result = simMTB.connectInput(int inputMtbServerHandle, int inputBitNumber, int outputMtbServerHandle, int outputBitNumber, int connectionType)"""
        ...

    def disconnectInput(self, inputMtbServerHandle: int, inputBitNumber: int) -> bool:
        """bool result = simMTB.disconnectInput(int inputMtbServerHandle, int inputBitNumber)"""
        ...

    def getInput(self, mtbServerHandle: int) -> Any:
        """int[4] inputValues = simMTB.getInput(int mtbServerHandle)"""
        ...

    def getJoints(self, mtbServerHandle: int) -> Any:
        """float[4] jointValues = simMTB.getJoints(int mtbServerHandle)"""
        ...

    def getOutput(self, mtbServerHandle: int) -> Any:
        """int[4] outputValues = simMTB.getOutput(int mtbServerHandle)"""
        ...

    def setInput(self, mtbServerHandle: int, inputValues: Any) -> bool:
        """bool result = simMTB.setInput(int mtbServerHandle, int[4] inputValues)"""
        ...

    def startServer(self, mtbServerExecutable: str, portNumber: int, program: bytes, jointPositions: Any, velocities: Any) -> Tuple[int, str]:
        """int mtbServerHandle, string message = simMTB.startServer(string mtbServerExecutable, int portNumber, buffer program, float[4] jointPositions, float[2] velocities)"""
        ...

    def step(self, mtbServerHandle: int, timeStep: float) -> Tuple[int, str]:
        """int result, string message = simMTB.step(int mtbServerHandle, float timeStep)"""
        ...

    def stopServer(self, mtbServerHandle: int) -> bool:
        """bool result = simMTB.stopServer(int mtbServerHandle)"""
        ...


class simMujoco:
    """API functions for the `simMujoco` module."""

    # --- Functions ---
    def addFlexcomp(self, info: dict) -> int:
        """int injectionId = simMujoco.addFlexcomp(map info)"""
        ...

    def addInjection(self, info: dict) -> int:
        """int injectionId = simMujoco.addInjection(map info)"""
        ...

    def composite(self, xml: str, info: dict) -> int:
        """int injectionId = simMujoco.composite(string xml, map info)"""
        ...

    def getCompositeInfo(self, injectionId: int, what: int) -> dict:
        """map info = simMujoco.getCompositeInfo(int injectionId, int what)"""
        ...

    def getFlexcompInfo(self, injectionId: int, what: int) -> dict:
        """map info = simMujoco.getFlexcompInfo(int injectionId, int what)"""
        ...

    def getInfo(self, what: str) -> str:
        """string info = simMujoco.getInfo(string what)"""
        ...

    def removeInjection(self, injectionId: int) -> None:
        """simMujoco.removeInjection(int injectionId)"""
        ...


class simOMPL:
    """API functions for the `simOMPL` module."""

    # --- Constants ---
    Algorithm_BITstar: int
    Algorithm_BKPIECE1: int
    Algorithm_BiTRRT: int
    Algorithm_CForest: int
    Algorithm_EST: int
    Algorithm_FMT: int
    Algorithm_KPIECE1: int
    Algorithm_LBKPIECE1: int
    Algorithm_LBTRRT: int
    Algorithm_LazyPRM: int
    Algorithm_LazyPRMstar: int
    Algorithm_LazyRRT: int
    Algorithm_PDST: int
    Algorithm_PRM: int
    Algorithm_PRMstar: int
    Algorithm_RRT: int
    Algorithm_RRTConnect: int
    Algorithm_RRTstar: int
    Algorithm_SBL: int
    Algorithm_SPARS: int
    Algorithm_SPARStwo: int
    Algorithm_STRIDE: int
    Algorithm_TRRT: int
    StateSpaceType_cyclic_joint_position: int
    StateSpaceType_dubins: int
    StateSpaceType_joint_position: int
    StateSpaceType_pose2d: int
    StateSpaceType_pose3d: int
    StateSpaceType_position2d: int
    StateSpaceType_position3d: int
    pluginHandle: int

    # --- Functions ---
    def addGoalState(self, taskHandle: str, state: list) -> None:
        """simOMPL.addGoalState(string taskHandle, float[] state)"""
        ...

    def compute(self, taskHandle: str, maxTime: float, maxSimplificationTime: float = -1.0, stateCnt: int = 0) -> Tuple[bool, list]:
        """bool solved, float[] states = simOMPL.compute(string taskHandle, float maxTime, float maxSimplificationTime=-1.0, int stateCnt=0)"""
        ...

    def createStateSpace(self, name: str, type: int, objectHandle: int, boundsLow: list, boundsHigh: list, useForProjection: int, weight: float = 1.0, refObjectHandle: int = -1) -> str:
        """string stateSpaceHandle = simOMPL.createStateSpace(string name, int type, int objectHandle, float[] boundsLow, float[] boundsHigh, int useForProjection, float weight=1.0, int refObjectHandle=-1)"""
        ...

    def createStateSpaceForJoint(self, name: str, jointHandle: int, useForProjection: int = 0, weight: float = 1) -> int:
        """int ssHandle = simOMPL.createStateSpaceForJoint(string name, int jointHandle, int useForProjection=0, float weight=1)"""
        ...

    def createTask(self, name: str) -> str:
        """string taskHandle = simOMPL.createTask(string name)"""
        ...

    def destroyStateSpace(self, stateSpaceHandle: str) -> None:
        """simOMPL.destroyStateSpace(string stateSpaceHandle)"""
        ...

    def destroyTask(self, taskHandle: str) -> None:
        """simOMPL.destroyTask(string taskHandle)"""
        ...

    def drawPath(self, taskHandle: str, path: list, lineSize: float, color: Any, extraAttributes: int) -> list:
        """int[] dwos = simOMPL.drawPath(string taskHandle, float[] path, float lineSize, float[3] color, int extraAttributes)"""
        ...

    def drawPlannerData(self, taskHandle: str, pointSize: float, lineSize: float, color: Any, startColor: Any, goalColor: Any) -> list:
        """int[] dwos = simOMPL.drawPlannerData(string taskHandle, float pointSize, float lineSize, float[3] color, float[3] startColor, float[3] goalColor)"""
        ...

    def enforceBounds(self, taskHandle: str, state: list) -> list:
        """float[] state = simOMPL.enforceBounds(string taskHandle, float[] state)"""
        ...

    def getGoalDistance(self, taskHandle: str) -> float:
        """float distance = simOMPL.getGoalDistance(string taskHandle)"""
        ...

    def getPath(self, taskHandle: str) -> list:
        """float[] states = simOMPL.getPath(string taskHandle)"""
        ...

    def getPathState(self, taskHandle: str, path: list, index: int) -> list:
        """float[] state = simOMPL.getPathState(string taskHandle, float[] path, int index)"""
        ...

    def getPathStateCount(self, taskHandle: str, path: list) -> int:
        """int count = simOMPL.getPathStateCount(string taskHandle, float[] path)"""
        ...

    def getPlannerData(self, taskHandle: str) -> Tuple[list, list, list, list, list, list, list]:
        """float[] states, int[] tags, float[] tagsReal, int[] edges, float[] edgeWeights, int[] startVertices, int[] goalVertices = simOMPL.getPlannerData(string taskHandle)"""
        ...

    def getProjectedPathLength(self, taskHandle: str, path: list) -> None:
        """simOMPL.getProjectedPathLength(string taskHandle, float[] path)"""
        ...

    def getReversedPath(self, taskHandle: str, path: list) -> list:
        """float[] reversedPath = simOMPL.getReversedPath(string taskHandle, float[] path)"""
        ...

    def getStateSpaceDimension(self, taskHandle: str) -> int:
        """int dim = simOMPL.getStateSpaceDimension(string taskHandle)"""
        ...

    def hasApproximateSolution(self, taskHandle: str) -> bool:
        """bool result = simOMPL.hasApproximateSolution(string taskHandle)"""
        ...

    def hasExactSolution(self, taskHandle: str) -> bool:
        """bool result = simOMPL.hasExactSolution(string taskHandle)"""
        ...

    def hasSolution(self, taskHandle: str) -> bool:
        """bool result = simOMPL.hasSolution(string taskHandle)"""
        ...

    def interpolatePath(self) -> Tuple[Any, int]:
        """simOMPL.interpolatePath(string taskHandle, int stateCnt=0)"""
        ...

    def isStateValid(self, taskHandle: str, state: list) -> bool:
        """bool valid = simOMPL.isStateValid(string taskHandle, float[] state)"""
        ...

    def isStateWithinBounds(self, taskHandle: str, state: list) -> bool:
        """bool valid = simOMPL.isStateWithinBounds(string taskHandle, float[] state)"""
        ...

    def printTaskInfo(self, taskHandle: str) -> None:
        """simOMPL.printTaskInfo(string taskHandle)"""
        ...

    def projectStates(self, taskHandle: str, state: list) -> list:
        """float[] projection = simOMPL.projectStates(string taskHandle, float[] state)"""
        ...

    def projectionSize(self, taskHandle: str) -> int:
        """int size = simOMPL.projectionSize(string taskHandle)"""
        ...

    def readState(self, taskHandle: str) -> list:
        """float[] state = simOMPL.readState(string taskHandle)"""
        ...

    def removeDrawingObjects(self, taskHandle: str, dwos: list) -> None:
        """simOMPL.removeDrawingObjects(string taskHandle, int[] dwos)"""
        ...

    def setAlgorithm(self, taskHandle: str, algorithm: int) -> None:
        """simOMPL.setAlgorithm(string taskHandle, int algorithm)"""
        ...

    def setCollisionPairs(self, taskHandle: str, collisionPairHandles: list) -> None:
        """simOMPL.setCollisionPairs(string taskHandle, int[] collisionPairHandles)"""
        ...

    def setDubinsParams(self, stateSpaceHandle: str, turningRadius: float, isSymmetric: bool) -> None:
        """simOMPL.setDubinsParams(string stateSpaceHandle, float turningRadius, bool isSymmetric)"""
        ...

    def setGoal(self) -> Tuple[Any, int, int, float]:
        """simOMPL.setGoal(string taskHandle, int robotDummy, int goalDummy, float tolerance=0.001, float[] metric={1.0, 1.0, 1.0, 0.1}, int refDummy=-1)"""
        ...

    def setGoalCallback(self, taskHandle: str, callback: Any) -> None:
        """simOMPL.setGoalCallback(string taskHandle, func callback)"""
        ...

    def setGoalState(self, taskHandle: str, state: list) -> None:
        """simOMPL.setGoalState(string taskHandle, float[] state)"""
        ...

    def setGoalStates(self, taskHandle: str, states: list) -> None:
        """simOMPL.setGoalStates(string taskHandle, any[1..*] states)"""
        ...

    def setProjectionEvaluationCallback(self, taskHandle: str, callback: Any, projectionSize: int) -> None:
        """simOMPL.setProjectionEvaluationCallback(string taskHandle, func callback, int projectionSize)"""
        ...

    def setStartState(self, taskHandle: str, state: list) -> None:
        """simOMPL.setStartState(string taskHandle, float[] state)"""
        ...

    def setStateSpace(self, taskHandle: str, stateSpaceHandles: list) -> None:
        """simOMPL.setStateSpace(string taskHandle, string[] stateSpaceHandles)"""
        ...

    def setStateSpaceForJoints(self) -> Tuple[Any, list, list]:
        """simOMPL.setStateSpaceForJoints(string taskHandle, int[] jointHandles, int[] useForProjection={}, float[] weight={})"""
        ...

    def setStateValidationCallback(self, taskHandle: str, callback: Any) -> None:
        """simOMPL.setStateValidationCallback(string taskHandle, func callback)"""
        ...

    def setStateValidityCheckingResolution(self, taskHandle: str, resolution: float) -> None:
        """simOMPL.setStateValidityCheckingResolution(string taskHandle, float resolution)"""
        ...

    def setValidStateSamplerCallback(self, taskHandle: str, callback: Any, callbackNear: Any) -> None:
        """simOMPL.setValidStateSamplerCallback(string taskHandle, func callback, func callbackNear)"""
        ...

    def setVerboseLevel(self, taskHandle: str, verboseLevel: int) -> None:
        """simOMPL.setVerboseLevel(string taskHandle, int verboseLevel)"""
        ...

    def setup(self, taskHandle: str) -> None:
        """simOMPL.setup(string taskHandle)"""
        ...

    def simplifyPath(self) -> Tuple[Any, float]:
        """simOMPL.simplifyPath(string taskHandle, float maxSimplificationTime=-1.0)"""
        ...

    def solve(self, taskHandle: str, maxTime: float) -> bool:
        """bool solved = simOMPL.solve(string taskHandle, float maxTime)"""
        ...

    def stateDistance(self, taskHandle: str, a: list, b: list) -> float:
        """float distance = simOMPL.stateDistance(string taskHandle, float[] a, float[] b)"""
        ...

    def writeState(self, taskHandle: str, state: list) -> None:
        """simOMPL.writeState(string taskHandle, float[] state)"""
        ...


class simOpenMesh:
    """API functions for the `simOpenMesh` module."""

    # --- Functions ---
    # Could not generate stub for: simOpenMesh.decimate
    # Original signature: int decimatedShape = simOpenMesh.decimate(int inputShape, map params = nil)


class simPython:
    """API functions for the `simPython` module."""

    # --- Functions ---
    def call(self, scriptStateHandle: str, func: str, args: dict) -> dict:
        """map result = simPython.call(string scriptStateHandle, string func, map args)"""
        ...

    def create(self) -> str:
        """string scriptStateHandle = simPython.create()"""
        ...

    def destroy(self, scriptStateHandle: str) -> None:
        """simPython.destroy(string scriptStateHandle)"""
        ...

    def getVersion(self) -> list:
        """int[] version = simPython.getVersion()"""
        ...

    def run(self, scriptStateHandle: str, code: str) -> dict:
        """map result = simPython.run(string scriptStateHandle, string code)"""
        ...


class simQML:
    """API functions for the `simQML` module."""

    # --- Constants ---
    image_data_format_argb32: int
    image_data_format_bgr888: int
    image_data_format_gray8: int
    image_data_format_rgb32: int
    image_data_format_rgb888: int
    image_data_format_rgbx8888: int
    pluginHandle: int

    # --- Functions ---
    def createEngine(self) -> str:
        """string handle = simQML.createEngine()"""
        ...

    def destroyEngine(self, handle: str) -> None:
        """simQML.destroyEngine(string handle)"""
        ...

    def imageDataURL(self, data: bytes, width: int, height: int, format: str = "BMP", data_format: int = simqml_image_data_format_rgb888) -> str:
        """string dataURL = simQML.imageDataURL(buffer data, int width, int height, string format="BMP", int data_format=simqml_image_data_format_rgb888)"""
        ...

    def load(self, engineHandle: str, filename: str) -> None:
        """simQML.load(string engineHandle, string filename)"""
        ...

    def loadData(self) -> Tuple[Any, str, str]:
        """simQML.loadData(string engineHandle, string data, string basepath="")"""
        ...

    def qtVersion(self) -> list:
        """int[] version = simQML.qtVersion()"""
        ...

    def sendEvent(self, engine: str, name: str, data: dict) -> None:
        """simQML.sendEvent(string engine, string name, map data)"""
        ...

    def sendEventRaw(self, engineHandle: str, eventName: str, eventData: str) -> None:
        """simQML.sendEventRaw(string engineHandle, string eventName, string eventData)"""
        ...

    def setEventHandler(self, engine: str, funcName: str) -> None:
        """simQML.setEventHandler(string engine, string funcName)"""
        ...

    def setEventHandlerRaw(self, engineHandle: str, functionName: str) -> None:
        """simQML.setEventHandlerRaw(string engineHandle, string functionName)"""
        ...


class simROS2:
    """API functions for the `simROS2` module."""

    # --- Functions ---
    def actionClientTreatUInt8ArrayAsString(self, actionClientHandle: str) -> None:
        """simROS2.actionClientTreatUInt8ArrayAsString(string actionClientHandle)"""
        ...

    def actionServerActionAbort(self, actionServerHandle: str, goalUUID: str, result: dict) -> None:
        """simROS2.actionServerActionAbort(string actionServerHandle, string goalUUID, map result)"""
        ...

    def actionServerActionCanceled(self, actionServerHandle: str, goalUUID: str, result: dict) -> None:
        """simROS2.actionServerActionCanceled(string actionServerHandle, string goalUUID, map result)"""
        ...

    def actionServerActionExecute(self, actionServerHandle: str, goalUUID: str) -> None:
        """simROS2.actionServerActionExecute(string actionServerHandle, string goalUUID)"""
        ...

    def actionServerActionIsActive(self, actionServerHandle: str, goalUUID: str) -> bool:
        """bool result = simROS2.actionServerActionIsActive(string actionServerHandle, string goalUUID)"""
        ...

    def actionServerActionIsCanceling(self, actionServerHandle: str, goalUUID: str) -> bool:
        """bool result = simROS2.actionServerActionIsCanceling(string actionServerHandle, string goalUUID)"""
        ...

    def actionServerActionIsExecuting(self, actionServerHandle: str, goalUUID: str) -> bool:
        """bool result = simROS2.actionServerActionIsExecuting(string actionServerHandle, string goalUUID)"""
        ...

    def actionServerActionSucceed(self, actionServerHandle: str, goalUUID: str, result: dict) -> None:
        """simROS2.actionServerActionSucceed(string actionServerHandle, string goalUUID, map result)"""
        ...

    def actionServerPublishFeedback(self, actionServerHandle: str, goalUUID: str, feedback: dict) -> None:
        """simROS2.actionServerPublishFeedback(string actionServerHandle, string goalUUID, map feedback)"""
        ...

    def actionServerTreatUInt8ArrayAsString(self, actionServerHandle: str) -> None:
        """simROS2.actionServerTreatUInt8ArrayAsString(string actionServerHandle)"""
        ...

    def call(self, clientHandle: str, request: dict) -> dict:
        """map result = simROS2.call(string clientHandle, map request)"""
        ...

    def cancelLastGoal(self, actionClientHandle: str) -> bool:
        """bool success = simROS2.cancelLastGoal(string actionClientHandle)"""
        ...

    def clientTreatUInt8ArrayAsString(self, clientHandle: str) -> None:
        """simROS2.clientTreatUInt8ArrayAsString(string clientHandle)"""
        ...

    def createActionClient(self, actionName: str, actionType: str, goalResponseCallback: Any, feedbackCallback: Any, resultCallback: Any) -> str:
        """string actionClientHandle = simROS2.createActionClient(string actionName, string actionType, func goalResponseCallback, func feedbackCallback, func resultCallback)"""
        ...

    def createActionServer(self, actionName: str, actionType: str, handleGoalCallback: Any, handleCancelCallback: Any, handleAcceptedCallback: Any) -> str:
        """string actionServerHandle = simROS2.createActionServer(string actionName, string actionType, func handleGoalCallback, func handleCancelCallback, func handleAcceptedCallback)"""
        ...

    def createClient(self, serviceName: str, serviceType: str) -> str:
        """string clientHandle = simROS2.createClient(string serviceName, string serviceType)"""
        ...

    def createInterface(self, type: str) -> dict:
        """map result = simROS2.createInterface(string type)"""
        ...

    def createPublisher(self, topicName: str, topicType: str, unused: int = 0, unused2: bool = false, qos: dict = nil) -> str:
        """string publisherHandle = simROS2.createPublisher(string topicName, string topicType, int unused=0, bool unused2=false, map qos=nil)"""
        ...

    def createService(self, serviceName: str, serviceType: str, serviceCallback: Any) -> str:
        """string serviceHandle = simROS2.createService(string serviceName, string serviceType, func serviceCallback)"""
        ...

    def createSubscription(self, topicName: str, topicType: str, topicCallback: Any, unused: int = 0, qos: dict = nil) -> str:
        """string subscriptionHandle = simROS2.createSubscription(string topicName, string topicType, func topicCallback, int unused=0, map qos=nil)"""
        ...

    def deleteParam(self, name: str) -> None:
        """simROS2.deleteParam(string name)"""
        ...

    def getInterfaceConstants(self, type: str) -> dict:
        """map result = simROS2.getInterfaceConstants(string type)"""
        ...

    def getParamBool(self, name: str, defaultValue: bool = false) -> Tuple[bool, bool]:
        """bool exists, bool value = simROS2.getParamBool(string name, bool defaultValue=false)"""
        ...

    def getParamDouble(self, name: str, defaultValue: float = 0.0) -> Tuple[bool, float]:
        """bool exists, float value = simROS2.getParamDouble(string name, float defaultValue=0.0)"""
        ...

    def getParamInt(self, name: str, defaultValue: int = 0) -> Tuple[bool, int]:
        """bool exists, int value = simROS2.getParamInt(string name, int defaultValue=0)"""
        ...

    def getParamString(self, name: str, defaultValue: str = "") -> Tuple[bool, str]:
        """bool exists, string value = simROS2.getParamString(string name, string defaultValue="")"""
        ...

    def getSimulationTime(self) -> None:
        """simROS2.getSimulationTime()"""
        ...

    def getSystemTime(self) -> None:
        """simROS2.getSystemTime()"""
        ...

    def getTime(self, clock_type: int = simros2_clock_ros) -> dict:
        """map time = simROS2.getTime(int clock_type=simros2_clock_ros)"""
        ...

    def hasParam(self, name: str) -> bool:
        """bool exists = simROS2.hasParam(string name)"""
        ...

    def imageTransportCreatePublisher(self, topicName: str, queueSize: int = 1) -> str:
        """string publisherHandle = simROS2.imageTransportCreatePublisher(string topicName, int queueSize=1)"""
        ...

    def imageTransportCreateSubscription(self, topicName: str, topicCallback: Any, queueSize: int = 1) -> str:
        """string subscriptionHandle = simROS2.imageTransportCreateSubscription(string topicName, func topicCallback, int queueSize=1)"""
        ...

    def imageTransportPublish(self, publisherHandle: str, data: bytes, width: int, height: int, frame_id: str) -> None:
        """simROS2.imageTransportPublish(string publisherHandle, buffer data, int width, int height, string frame_id)"""
        ...

    def imageTransportShutdownPublisher(self, publisherHandle: str) -> None:
        """simROS2.imageTransportShutdownPublisher(string publisherHandle)"""
        ...

    def imageTransportShutdownSubscription(self, subscriptionHandle: str) -> None:
        """simROS2.imageTransportShutdownSubscription(string subscriptionHandle)"""
        ...

    def importInterface(self, name: str) -> None:
        """simROS2.importInterface(string name)"""
        ...

    def publish(self, publisherHandle: str, message: dict) -> None:
        """simROS2.publish(string publisherHandle, map message)"""
        ...

    def publisherTreatUInt8ArrayAsString(self, publisherHandle: str) -> None:
        """simROS2.publisherTreatUInt8ArrayAsString(string publisherHandle)"""
        ...

    def sendGoal(self, actionClientHandle: str, goal: dict) -> bool:
        """bool success = simROS2.sendGoal(string actionClientHandle, map goal)"""
        ...

    def sendTransform(self, transform: dict) -> None:
        """simROS2.sendTransform(map transform)"""
        ...

    def sendTransforms(self, transforms: dict) -> None:
        """simROS2.sendTransforms(map transforms)"""
        ...

    def serviceTreatUInt8ArrayAsString(self, serviceHandle: str) -> None:
        """simROS2.serviceTreatUInt8ArrayAsString(string serviceHandle)"""
        ...

    def setParamBool(self, name: str, value: bool) -> None:
        """simROS2.setParamBool(string name, bool value)"""
        ...

    def setParamDouble(self, name: str, value: float) -> None:
        """simROS2.setParamDouble(string name, float value)"""
        ...

    def setParamInt(self, name: str, value: int) -> None:
        """simROS2.setParamInt(string name, int value)"""
        ...

    def setParamString(self, name: str, value: str) -> None:
        """simROS2.setParamString(string name, string value)"""
        ...

    def shutdownActionClient(self, actionClientHandle: str) -> None:
        """simROS2.shutdownActionClient(string actionClientHandle)"""
        ...

    def shutdownActionServer(self, actionServerHandle: str) -> None:
        """simROS2.shutdownActionServer(string actionServerHandle)"""
        ...

    def shutdownClient(self, clientHandle: str) -> None:
        """simROS2.shutdownClient(string clientHandle)"""
        ...

    def shutdownPublisher(self, publisherHandle: str) -> None:
        """simROS2.shutdownPublisher(string publisherHandle)"""
        ...

    def shutdownService(self, serviceHandle: str) -> None:
        """simROS2.shutdownService(string serviceHandle)"""
        ...

    def shutdownSubscription(self, subscriptionHandle: str) -> None:
        """simROS2.shutdownSubscription(string subscriptionHandle)"""
        ...

    def spinSome(self) -> None:
        """simROS2.spinSome()"""
        ...

    def subscriptionTreatUInt8ArrayAsString(self, subscriptionHandle: str) -> None:
        """simROS2.subscriptionTreatUInt8ArrayAsString(string subscriptionHandle)"""
        ...

    def supportedInterfaces(self) -> list:
        """string[] result = simROS2.supportedInterfaces()"""
        ...

    def timeFromFloat(self, t: float) -> None:
        """simROS2.timeFromFloat(float t)"""
        ...

    def timeToFloat(self, t: dict) -> None:
        """simROS2.timeToFloat(map t)"""
        ...

    def waitForService(self, clientHandle: str, timeout: float) -> bool:
        """bool result = simROS2.waitForService(string clientHandle, float timeout)"""
        ...


class simRRS1:
    """API functions for the `simRRS1` module."""

    # --- Functions ---
    def CANCEL_EVENT(self, rcsHandle: bytes, eventId: int) -> int:
        """int status = simRRS1.CANCEL_EVENT(buffer rcsHandle, int eventId)"""
        ...

    def CANCEL_FLYBY_CRITERIA(self, rcsHandle: bytes, paramNumber: int) -> int:
        """int status = simRRS1.CANCEL_FLYBY_CRITERIA(buffer rcsHandle, int paramNumber)"""
        ...

    def CANCEL_MOTION(self, rcsHandle: bytes) -> int:
        """int status = simRRS1.CANCEL_MOTION(buffer rcsHandle)"""
        ...

    def CONTINUE_MOTION(self, rcsHandle: bytes) -> int:
        """int status = simRRS1.CONTINUE_MOTION(buffer rcsHandle)"""
        ...

    def CONTROLLER_POSITION_TO_MATRIX(self, rcsHandle: bytes, contrPos: str) -> Tuple[int, bytes, str]:
        """int status, buffer cartPos, string configuration = simRRS1.CONTROLLER_POSITION_TO_MATRIX(buffer rcsHandle, string contrPos)"""
        ...

    def DEBUG(self, rcsHandle: bytes, debugFlags: bytes, opcodeSelect: int, logFileName: str) -> int:
        """int status = simRRS1.DEBUG(buffer rcsHandle, buffer debugFlags, int opcodeSelect, string logFileName)"""
        ...

    def DEFINE_EVENT(self, rcsHandle: bytes, eventId: int, targetId: int, resolution: float, typeOfEvent: int, eventSpec: Any) -> int:
        """int status = simRRS1.DEFINE_EVENT(buffer rcsHandle, int eventId, int targetId, float resolution, int typeOfEvent, float[16] eventSpec)"""
        ...

    def EXTENDED_SERVICE(self, rcsHandle: bytes, inData: str) -> Tuple[int, str]:
        """int status, string outData = simRRS1.EXTENDED_SERVICE(buffer rcsHandle, string inData)"""
        ...

    def GET_CELL_FRAME(self, rcsHandle: bytes, storage: int, firstNext: int, frameId: str) -> Tuple[int, str, int, str, bytes, bytes]:
        """int status, string frameId, int frameType, string relativeToId, buffer jointNumber, buffer frameData = simRRS1.GET_CELL_FRAME(buffer rcsHandle, int storage, int firstNext, string frameId)"""
        ...

    def GET_CURRENT_TARGETID(self, rcsHandle: bytes) -> Tuple[int, int]:
        """int status, int targetId = simRRS1.GET_CURRENT_TARGETID(buffer rcsHandle)"""
        ...

    def GET_EVENT(self, rcsHandle: bytes, eventNumber: int) -> Tuple[int, int, float]:
        """int status, int eventId, float timeTillEvent = simRRS1.GET_EVENT(buffer rcsHandle, int eventNumber)"""
        ...

    def GET_FORWARD_KINEMATIC(self, rcsHandle: bytes, jointPos: bytes) -> Tuple[int, bytes, bytes, str, bytes, int]:
        """int status, buffer cartPos, buffer jointPos, string configuration, buffer jointLimit, int numberOfMessages = simRRS1.GET_FORWARD_KINEMATIC(buffer rcsHandle, buffer jointPos)"""
        ...

    def GET_HOME_JOINT_POSITION(self, rcsHandle: bytes) -> Tuple[int, bytes]:
        """int status, buffer homePosition = simRRS1.GET_HOME_JOINT_POSITION(buffer rcsHandle)"""
        ...

    def GET_INVERSE_KINEMATIC(self, rcsHandle: bytes, cartPos: bytes, jointPos: bytes, configuration: str, outputFormat: bytes) -> Tuple[int, bytes, bytes, int]:
        """int status, buffer jointPos, buffer jointLimit, int numberOfMessages = simRRS1.GET_INVERSE_KINEMATIC(buffer rcsHandle, buffer cartPos, buffer jointPos, string configuration, buffer outputFormat)"""
        ...

    def GET_MESSAGE(self, rcsHandle: bytes, messageNumber: int) -> Tuple[int, int, str]:
        """int status, int severity, string text = simRRS1.GET_MESSAGE(buffer rcsHandle, int messageNumber)"""
        ...

    def GET_NEXT_STEP(self, rcsHandle: bytes, outputFormat: bytes) -> Tuple[int, bytes, bytes, str, float, bytes, int, int]:
        """int status, buffer cartPos, buffer jointPos, string configuration, float elapsedTime, buffer jointLimit, int numberOfEvents, int numberOfMessages = simRRS1.GET_NEXT_STEP(buffer rcsHandle, buffer outputFormat)"""
        ...

    def GET_RCS_DATA(self, rcsHandle: bytes, storage: int, firstNext: int, paramId: str) -> Tuple[int, str, str, int]:
        """int status, string paramId, string paramContents, int permission = simRRS1.GET_RCS_DATA(buffer rcsHandle, int storage, int firstNext, string paramId)"""
        ...

    def GET_ROBOT_STAMP(self, rcsHandle: bytes) -> Tuple[int, str, str, str]:
        """int status, string manipulator, string controller, string software = simRRS1.GET_ROBOT_STAMP(buffer rcsHandle)"""
        ...

    def INITIALIZE(self, robotNumber: int, robotPathName: str, modulePathName: str, manipulatorType: str, CarrrsVersion: int, debug: int) -> Tuple[int, bytes, int, int, int]:
        """int status, buffer rcsHandle, int rcsRrsVersion, int rcsVersion, int numberOfMessages = simRRS1.INITIALIZE(int robotNumber, string robotPathName, string modulePathName, string manipulatorType, int CarrrsVersion, int debug)"""
        ...

    def LOAD_RCS_DATA(self, rcsHandle: bytes) -> Tuple[int, int]:
        """int status, int numberOfMessages = simRRS1.LOAD_RCS_DATA(buffer rcsHandle)"""
        ...

    def MATRIX_TO_CONTROLLER_POSITION(self, rcsHandle: bytes, cartPos: bytes, configuration: str) -> Tuple[int, str]:
        """int status, string contrPos = simRRS1.MATRIX_TO_CONTROLLER_POSITION(buffer rcsHandle, buffer cartPos, string configuration)"""
        ...

    def MODIFY_CELL_FRAME(self, rcsHandle: bytes, storage: int, frameId: str, frameData: bytes) -> int:
        """int status = simRRS1.MODIFY_CELL_FRAME(buffer rcsHandle, int storage, string frameId, buffer frameData)"""
        ...

    def MODIFY_RCS_DATA(self, rcsHandle: bytes, storage: int, paramId: str, paramContents: str) -> int:
        """int status = simRRS1.MODIFY_RCS_DATA(buffer rcsHandle, int storage, string paramId, string paramContents)"""
        ...

    def RESET(self, rcsHandle: bytes, resetLevel: int) -> Tuple[int, int]:
        """int status, int numberOfMessages = simRRS1.RESET(buffer rcsHandle, int resetLevel)"""
        ...

    def REVERSE_MOTION(self, rcsHandle: bytes, distance: float) -> int:
        """int status = simRRS1.REVERSE_MOTION(buffer rcsHandle, float distance)"""
        ...

    def SAVE_RCS_DATA(self, rcsHandle: bytes) -> int:
        """int status = simRRS1.SAVE_RCS_DATA(buffer rcsHandle)"""
        ...

    def SELECT_DOMINANT_INTERPOLATION(self, rcsHandle: bytes, dominantIntType: int, dominantIntParam: int) -> int:
        """int status = simRRS1.SELECT_DOMINANT_INTERPOLATION(buffer rcsHandle, int dominantIntType, int dominantIntParam)"""
        ...

    def SELECT_FLYBY_CRITERIA(self, rcsHandle: bytes, paramNumber: int) -> int:
        """int status = simRRS1.SELECT_FLYBY_CRITERIA(buffer rcsHandle, int paramNumber)"""
        ...

    def SELECT_FLYBY_MODE(self, rcsHandle: bytes, flyByOn: int) -> int:
        """int status = simRRS1.SELECT_FLYBY_MODE(buffer rcsHandle, int flyByOn)"""
        ...

    def SELECT_MOTION_TYPE(self, rcsHandle: bytes, motionType: int) -> int:
        """int status = simRRS1.SELECT_MOTION_TYPE(buffer rcsHandle, int motionType)"""
        ...

    def SELECT_ORIENTATION_INTERPOLATION_MODE(self, rcsHandle: bytes, interpolationMode: int, oriConst: int) -> int:
        """int status = simRRS1.SELECT_ORIENTATION_INTERPOLATION_MODE(buffer rcsHandle, int interpolationMode, int oriConst)"""
        ...

    def SELECT_POINT_ACCURACY(self, rcsHandle: bytes, accuracyType: int) -> int:
        """int status = simRRS1.SELECT_POINT_ACCURACY(buffer rcsHandle, int accuracyType)"""
        ...

    def SELECT_TARGET_TYPE(self, rcsHandle: bytes, targetType: int, cartPos: bytes, jointPos: bytes, configuration: str) -> int:
        """int status = simRRS1.SELECT_TARGET_TYPE(buffer rcsHandle, int targetType, buffer cartPos, buffer jointPos, string configuration)"""
        ...

    def SELECT_TIME_COMPENSATION(self, rcsHandle: bytes, compensation: bytes) -> int:
        """int status = simRRS1.SELECT_TIME_COMPENSATION(buffer rcsHandle, buffer compensation)"""
        ...

    def SELECT_TRACKING(self, rcsHandle: bytes, conveyorFlags: bytes) -> int:
        """int status = simRRS1.SELECT_TRACKING(buffer rcsHandle, buffer conveyorFlags)"""
        ...

    def SELECT_TRAJECTORY_MODE(self, rcsHandle: bytes, trajectoryOn: int) -> int:
        """int status = simRRS1.SELECT_TRAJECTORY_MODE(buffer rcsHandle, int trajectoryOn)"""
        ...

    def SELECT_WEAVING_GROUP(self, rcsHandle: bytes, groupNo: int, groupOn: int) -> int:
        """int status = simRRS1.SELECT_WEAVING_GROUP(buffer rcsHandle, int groupNo, int groupOn)"""
        ...

    def SELECT_WEAVING_MODE(self, rcsHandle: bytes, weavingMode: int) -> int:
        """int status = simRRS1.SELECT_WEAVING_MODE(buffer rcsHandle, int weavingMode)"""
        ...

    def SELECT_WORK_FRAMES(self, rcsHandle: bytes, toolId: str, objectId: str) -> int:
        """int status = simRRS1.SELECT_WORK_FRAMES(buffer rcsHandle, string toolId, string objectId)"""
        ...

    def SET_ADVANCE_MOTION(self, rcsHandle: bytes, numberOfMotion: int) -> int:
        """int status = simRRS1.SET_ADVANCE_MOTION(buffer rcsHandle, int numberOfMotion)"""
        ...

    def SET_CARTESIAN_ORIENTATION_ACCELERATION(self, rcsHandle: bytes, rotationNo: int, accelValue: float, accelType: int) -> int:
        """int status = simRRS1.SET_CARTESIAN_ORIENTATION_ACCELERATION(buffer rcsHandle, int rotationNo, float accelValue, int accelType)"""
        ...

    def SET_CARTESIAN_ORIENTATION_SPEED(self, rcsHandle: bytes, rotationNo: int, speedValue: float) -> int:
        """int status = simRRS1.SET_CARTESIAN_ORIENTATION_SPEED(buffer rcsHandle, int rotationNo, float speedValue)"""
        ...

    def SET_CARTESIAN_POSITION_ACCELERATION(self, rcsHandle: bytes, accelValue: float, accelType: int) -> int:
        """int status = simRRS1.SET_CARTESIAN_POSITION_ACCELERATION(buffer rcsHandle, float accelValue, int accelType)"""
        ...

    def SET_CARTESIAN_POSITION_SPEED(self, rcsHandle: bytes, speedValue: float) -> int:
        """int status = simRRS1.SET_CARTESIAN_POSITION_SPEED(buffer rcsHandle, float speedValue)"""
        ...

    def SET_CONFIGURATION_CONTROL(self, rcsHandle: bytes, paramId: str, paramContents: str) -> int:
        """int status = simRRS1.SET_CONFIGURATION_CONTROL(buffer rcsHandle, string paramId, string paramContents)"""
        ...

    def SET_CONVEYOR_POSITION(self, rcsHandle: bytes, inputFormat: bytes, conveyorFlags: bytes, conveyorPos: Any) -> int:
        """int status = simRRS1.SET_CONVEYOR_POSITION(buffer rcsHandle, buffer inputFormat, buffer conveyorFlags, float[32] conveyorPos)"""
        ...

    def SET_FLYBY_CRITERIA_PARAMETER(self, rcsHandle: bytes, paramNumber: int, jointNr: int, paramValue: float) -> int:
        """int status = simRRS1.SET_FLYBY_CRITERIA_PARAMETER(buffer rcsHandle, int paramNumber, int jointNr, float paramValue)"""
        ...

    def SET_INITIAL_POSITION(self, rcsHandle: bytes, cartPos: bytes, jointPos: bytes, configuration: str) -> Tuple[int, bytes]:
        """int status, buffer jointLimit = simRRS1.SET_INITIAL_POSITION(buffer rcsHandle, buffer cartPos, buffer jointPos, string configuration)"""
        ...

    def SET_INTERPOLATION_TIME(self, rcsHandle: bytes, interpolationTime: float) -> int:
        """int status = simRRS1.SET_INTERPOLATION_TIME(buffer rcsHandle, float interpolationTime)"""
        ...

    def SET_JOINT_ACCELERATIONS(self, rcsHandle: bytes, allJointFlags: int, jointFlags: bytes, accelPercent: Any, accelType: int) -> int:
        """int status = simRRS1.SET_JOINT_ACCELERATIONS(buffer rcsHandle, int allJointFlags, buffer jointFlags, float[32] accelPercent, int accelType)"""
        ...

    def SET_JOINT_JERKS(self, rcsHandle: bytes, allJointFlags: int, jointFlags: bytes, jerkPercent: Any, jerkType: int) -> int:
        """int status = simRRS1.SET_JOINT_JERKS(buffer rcsHandle, int allJointFlags, buffer jointFlags, float[32] jerkPercent, int jerkType)"""
        ...

    def SET_JOINT_SPEEDS(self, rcsHandle: bytes, allJointFlags: int, jointFlags: bytes, speedPercent: Any) -> int:
        """int status = simRRS1.SET_JOINT_SPEEDS(buffer rcsHandle, int allJointFlags, buffer jointFlags, float[32] speedPercent)"""
        ...

    def SET_MOTION_FILTER(self, rcsHandle: bytes, filterFactor: int) -> int:
        """int status = simRRS1.SET_MOTION_FILTER(buffer rcsHandle, int filterFactor)"""
        ...

    def SET_MOTION_TIME(self, rcsHandle: bytes, timeValue: float) -> int:
        """int status = simRRS1.SET_MOTION_TIME(buffer rcsHandle, float timeValue)"""
        ...

    def SET_NEXT_TARGET(self, rcsHandle: bytes, targetId: int, targetParam: int, cartPos: bytes, jointPos: bytes, configuration: str, targetParamValue: float) -> int:
        """int status = simRRS1.SET_NEXT_TARGET(buffer rcsHandle, int targetId, int targetParam, buffer cartPos, buffer jointPos, string configuration, float targetParamValue)"""
        ...

    def SET_OVERRIDE_ACCELERATION(self, rcsHandle: bytes, correctionValue: float, accelType: int, correctionType: int) -> int:
        """int status = simRRS1.SET_OVERRIDE_ACCELERATION(buffer rcsHandle, float correctionValue, int accelType, int correctionType)"""
        ...

    def SET_OVERRIDE_POSITION(self, rcsHandle: bytes, posOffset: bytes) -> int:
        """int status = simRRS1.SET_OVERRIDE_POSITION(buffer rcsHandle, buffer posOffset)"""
        ...

    def SET_OVERRIDE_SPEED(self, rcsHandle: bytes, correctionValue: float, correctionType: int) -> int:
        """int status = simRRS1.SET_OVERRIDE_SPEED(buffer rcsHandle, float correctionValue, int correctionType)"""
        ...

    def SET_PAYLOAD_PARAMETER(self, rcsHandle: bytes, storage: int, frameId: str, paramNumber: int, paramValue: float) -> int:
        """int status = simRRS1.SET_PAYLOAD_PARAMETER(buffer rcsHandle, int storage, string frameId, int paramNumber, float paramValue)"""
        ...

    def SET_POINT_ACCURACY_PARAMETER(self, rcsHandle: bytes, accuracyType: int, accuracyValue: float) -> int:
        """int status = simRRS1.SET_POINT_ACCURACY_PARAMETER(buffer rcsHandle, int accuracyType, float accuracyValue)"""
        ...

    def SET_REST_PARAMETER(self, rcsHandle: bytes, paramNumber: int, paramValue: float) -> int:
        """int status = simRRS1.SET_REST_PARAMETER(buffer rcsHandle, int paramNumber, float paramValue)"""
        ...

    def SET_WEAVING_GROUP_PARAMETER(self, rcsHandle: bytes, groupNo: int, paramNo: int, paramValue: float) -> int:
        """int status = simRRS1.SET_WEAVING_GROUP_PARAMETER(buffer rcsHandle, int groupNo, int paramNo, float paramValue)"""
        ...

    def STOP_MOTION(self, rcsHandle: bytes) -> int:
        """int status = simRRS1.STOP_MOTION(buffer rcsHandle)"""
        ...

    def TERMINATE(self, rcsHandle: bytes) -> int:
        """int status = simRRS1.TERMINATE(buffer rcsHandle)"""
        ...

    def selectRcsServer(self, rcsServerHandle: int) -> bool:
        """bool result = simRRS1.selectRcsServer(int rcsServerHandle)"""
        ...

    def startRcsServer(self, rcsLibraryFilename: str, rcsLibraryFunctionName: str, portNumber: int) -> int:
        """int rcsServerHandle = simRRS1.startRcsServer(string rcsLibraryFilename, string rcsLibraryFunctionName, int portNumber)"""
        ...

    def stopRcsServer(self, rcsServerHandle: int) -> bool:
        """bool result = simRRS1.stopRcsServer(int rcsServerHandle)"""
        ...


class simRemoteApi:
    """API functions for the `simRemoteApi` module."""

    # --- Functions ---
    def reset(self, socketPort: int) -> int:
        """int result=simRemoteApi.reset(int socketPort)"""
        ...

    def start(self, socketPort: int, maxPacketSize: int = 1300, debug: bool = false, preEnableTrigger: bool = false) -> int:
        """int result=simRemoteApi.start(int socketPort,int maxPacketSize=1300,bool debug=false,bool preEnableTrigger=false)"""
        ...

    def status(self, socketPort: int) -> Tuple[int, Any, int, int, str]:
        """int status,int[5] info,int version,int clientVersion,string connectedIp=simRemoteApi.status(int socketPort)"""
        ...

    def stop(self, socketPort: int) -> int:
        """int result=simRemoteApi.stop(int socketPort)"""
        ...


class simSDF:
    """API functions for the `simSDF` module."""

    # --- Functions ---
    def dump(self, fileName: str) -> None:
        """simSDF.dump(string fileName)"""
        ...

    def import(self) -> Tuple[Any, dict]:
        """simSDF.import(string fileName, map options={})"""
        ...


class simSubprocess:
    """API functions for the `simSubprocess` module."""

    # --- Functions ---
    def exec(self, programPath: str, args: list, input: bytes = "", opts: dict = ...) -> Tuple[int, bytes]:
        """int exitCode, buffer output = simSubprocess.exec(string programPath, string[] args, buffer input="", map opts={})"""
        ...

    def execAsync(self, programPath: str, args: list, opts: dict = ...) -> str:
        """string handle = simSubprocess.execAsync(string programPath, string[] args, map opts={})"""
        ...

    def getpid(self, handle: str) -> int:
        """int pid = simSubprocess.getpid(string handle)"""
        ...

    def isRunning(self, handle: str) -> bool:
        """bool running = simSubprocess.isRunning(string handle)"""
        ...

    def kill(self, handle: str) -> int:
        """int exitCode = simSubprocess.kill(string handle)"""
        ...

    def wait(self, handle: str, timeout: float = 5) -> int:
        """int exitCode = simSubprocess.wait(string handle, float timeout=5)"""
        ...


class simSurfRec:
    """API functions for the `simSurfRec` module."""

    # --- Functions ---
    def reconstruct_scale_space(self, pointCloudHandle: int, iterations: int = 4, neighbors: int = 12, samples: int = 300, squared_radius: float = -1.0) -> int:
        """int shapeHandle = simSurfRec.reconstruct_scale_space(int pointCloudHandle, int iterations=4, int neighbors=12, int samples=300, float squared_radius=-1.0)"""
        ...


class simUI:
    """API functions for the `simUI` module."""

    # --- Constants ---
    curve_scatter_shape_circle: int
    curve_scatter_shape_cross: int
    curve_scatter_shape_cross_circle: int
    curve_scatter_shape_cross_square: int
    curve_scatter_shape_diamond: int
    curve_scatter_shape_disc: int
    curve_scatter_shape_dot: int
    curve_scatter_shape_none: int
    curve_scatter_shape_peace: int
    curve_scatter_shape_plus: int
    curve_scatter_shape_plus_circle: int
    curve_scatter_shape_plus_square: int
    curve_scatter_shape_square: int
    curve_scatter_shape_star: int
    curve_scatter_shape_triangle: int
    curve_scatter_shape_triangle_inverted: int
    curve_style_impulse: int
    curve_style_line: int
    curve_style_line_and_scatter: int
    curve_style_scatter: int
    curve_style_step_center: int
    curve_style_step_left: int
    curve_style_step_right: int
    curve_type_time: int
    curve_type_xy: int
    filedialog_type_folder: int
    filedialog_type_load: int
    filedialog_type_load_multiple: int
    filedialog_type_save: int
    line_style_dashed: int
    line_style_dotted: int
    line_style_solid: int
    mouse_left_button_down: int
    mouse_left_button_up: int
    mouse_move: int
    msgbox_buttons_ok: int
    msgbox_buttons_okcancel: int
    msgbox_buttons_yesno: int
    msgbox_buttons_yesnocancel: int
    msgbox_result_cancel: int
    msgbox_result_no: int
    msgbox_result_ok: int
    msgbox_result_yes: int
    msgbox_type_critical: int
    msgbox_type_info: int
    msgbox_type_question: int
    msgbox_type_warning: int
    pluginHandle: int
    scene3d_node_type_camera: int
    scene3d_node_type_camera_controller_first_person: int
    scene3d_node_type_camera_controller_orbit: int
    scene3d_node_type_entity: int
    scene3d_node_type_light_directional: int
    scene3d_node_type_light_point: int
    scene3d_node_type_light_spot: int
    scene3d_node_type_material_diffuse_map: int
    scene3d_node_type_material_gooch: int
    scene3d_node_type_material_phong: int
    scene3d_node_type_material_texture: int
    scene3d_node_type_mesh: int
    scene3d_node_type_mesh_cone: int
    scene3d_node_type_mesh_cuboid: int
    scene3d_node_type_mesh_cylinder: int
    scene3d_node_type_mesh_plane: int
    scene3d_node_type_mesh_sphere: int
    scene3d_node_type_mesh_torus: int
    scene3d_node_type_object_picker: int
    scene3d_node_type_texture2d: int
    scene3d_node_type_texture_image: int
    scene3d_node_type_transform: int

    # --- Functions ---
    def addCurve(self, handle: str, id: int, type: int, name: str, color: Any, style: int, options: dict) -> None:
        """simUI.addCurve(string handle, int id, int type, string name, int[3] color, int style, map options)"""
        ...

    def addCurveTimePoints(self, handle: str, id: int, name: str, x: list, y: list) -> None:
        """simUI.addCurveTimePoints(string handle, int id, string name, float[] x, float[] y)"""
        ...

    def addCurveXYPoints(self, handle: str, id: int, name: str, t: list, x: list, y: list) -> None:
        """simUI.addCurveXYPoints(string handle, int id, string name, float[] t, float[] x, float[] y)"""
        ...

    def addScene3DNode(self, handle: str, id: int, nodeId: int, parentNodeId: int, type: int) -> None:
        """simUI.addScene3DNode(string handle, int id, int nodeId, int parentNodeId, int type)"""
        ...

    def addTreeItem(self) -> Tuple[Any, int, int, list, int]:
        """simUI.addTreeItem(string handle, int id, int item_id, string[] text, int parent_id=0, bool expanded=false, bool suppressEvents=true)"""
        ...

    def adjustSize(self, handle: str) -> None:
        """simUI.adjustSize(string handle)"""
        ...

    def appendText(self) -> Tuple[Any, int, str, bool]:
        """simUI.appendText(string handle, int id, string text, bool suppressEvents=true)"""
        ...

    def bannerCreate(self, text: str, btnKeys: list = nil, btnLabels: list = nil, callback: str = nil) -> int:
        """int id = simUI.bannerCreate(string text, string[] btnKeys=nil, string[] btnLabels=nil, string callback=nil)"""
        ...

    def bannerDestroy(self, id: int) -> None:
        """simUI.bannerDestroy(int id)"""
        ...

    def clearCurve(self, handle: str, id: int, name: str) -> None:
        """simUI.clearCurve(string handle, int id, string name)"""
        ...

    def clearTable(self) -> Tuple[Any, int, bool]:
        """simUI.clearTable(string handle, int id, bool suppressEvents=true)"""
        ...

    def clearTree(self) -> Tuple[Any, int, bool]:
        """simUI.clearTree(string handle, int id, bool suppressEvents=true)"""
        ...

    def collapseAll(self) -> Tuple[Any, int, bool]:
        """simUI.collapseAll(string handle, int id, bool suppressEvents=true)"""
        ...

    def colorDialog(self, initColor: Any = ..., arg1: Any, arg2: Any, title: str = "Select, showAlphaChannel: bool = false, native: bool = true) -> Any:
        """float[3] result = simUI.colorDialog(float[3..4] initColor={1,1,1}, string title="Select color", bool showAlphaChannel=false, bool native=true)"""
        ...

    def create(self, xml: str) -> str:
        """string uiHandle = simUI.create(string xml)"""
        ...

    def destroy(self, handle: str) -> None:
        """simUI.destroy(string handle)"""
        ...

    def expandAll(self) -> Tuple[Any, int, bool]:
        """simUI.expandAll(string handle, int id, bool suppressEvents=true)"""
        ...

    def expandToDepth(self) -> Tuple[Any, int, int, bool]:
        """simUI.expandToDepth(string handle, int id, int depth, bool suppressEvents=true)"""
        ...

    def fileDialog(self, type: int, title: str, startPath: str, initName: str, extName: str, ext: str, native: bool = false) -> list:
        """string[] result = simUI.fileDialog(int type, string title, string startPath, string initName, string extName, string ext, bool native=false)"""
        ...

    def getCheckboxValue(self, handle: str, id: int) -> int:
        """int value = simUI.getCheckboxValue(string handle, int id)"""
        ...

    def getColumnCount(self, handle: str, id: int) -> int:
        """int count = simUI.getColumnCount(string handle, int id)"""
        ...

    def getComboboxItemCount(self, handle: str, id: int) -> int:
        """int count = simUI.getComboboxItemCount(string handle, int id)"""
        ...

    def getComboboxItemText(self, handle: str, id: int, index: int) -> str:
        """string text = simUI.getComboboxItemText(string handle, int id, int index)"""
        ...

    def getComboboxItems(self, handle: str, id: int) -> list:
        """string[] items = simUI.getComboboxItems(string handle, int id)"""
        ...

    def getComboboxSelectedIndex(self, handle: str, id: int) -> int:
        """int index = simUI.getComboboxSelectedIndex(string handle, int id)"""
        ...

    def getCurrentEditWidget(self, handle: str) -> int:
        """int id = simUI.getCurrentEditWidget(string handle)"""
        ...

    def getCurrentTab(self, handle: str, id: int) -> int:
        """int index = simUI.getCurrentTab(string handle, int id)"""
        ...

    def getCurveData(self, handle: str, id: int, name: str) -> Tuple[list, list, list]:
        """float[] t, float[] x, float[] y = simUI.getCurveData(string handle, int id, string name)"""
        ...

    def getEditValue(self, handle: str, id: int) -> str:
        """string value = simUI.getEditValue(string handle, int id)"""
        ...

    def getItem(self, handle: str, id: int, row: int, column: int) -> str:
        """string text = simUI.getItem(string handle, int id, int row, int column)"""
        ...

    def getKeyboardModifiers(self) -> dict:
        """map m = simUI.getKeyboardModifiers()"""
        ...

    def getLabelText(self, handle: str, id: int) -> str:
        """string text = simUI.getLabelText(string handle, int id)"""
        ...

    def getPosition(self, handle: str) -> Tuple[int, int]:
        """int x, int y = simUI.getPosition(string handle)"""
        ...

    def getPropertiesState(self, handle: str, id: int) -> str:
        """string state = simUI.getPropertiesState(string handle, int id)"""
        ...

    def getRadiobuttonValue(self, handle: str, id: int) -> int:
        """int value = simUI.getRadiobuttonValue(string handle, int id)"""
        ...

    def getRowCount(self, handle: str, id: int) -> int:
        """int count = simUI.getRowCount(string handle, int id)"""
        ...

    def getSize(self, handle: str) -> Tuple[int, int]:
        """int w, int h = simUI.getSize(string handle)"""
        ...

    def getSliderValue(self, handle: str, id: int) -> int:
        """int value = simUI.getSliderValue(string handle, int id)"""
        ...

    def getSpinboxValue(self, handle: str, id: int) -> float:
        """float value = simUI.getSpinboxValue(string handle, int id)"""
        ...

    def getTitle(self, handle: str) -> str:
        """string title = simUI.getTitle(string handle)"""
        ...

    def getWidgetVisibility(self, handle: str, id: int) -> bool:
        """bool visibility = simUI.getWidgetVisibility(string handle, int id)"""
        ...

    def growPlotRanges(self, handle: str, id: int, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
        """simUI.growPlotRanges(string handle, int id, float xmin, float xmax, float ymin, float ymax)"""
        ...

    def growPlotXRange(self, handle: str, id: int, xmin: float, xmax: float) -> None:
        """simUI.growPlotXRange(string handle, int id, float xmin, float xmax)"""
        ...

    def growPlotYRange(self, handle: str, id: int, ymin: float, ymax: float) -> None:
        """simUI.growPlotYRange(string handle, int id, float ymin, float ymax)"""
        ...

    def hide(self, handle: str) -> None:
        """simUI.hide(string handle)"""
        ...

    def inputDialog(self, initValue: str = "", label: str = "Input, title: str = "") -> str:
        """string result = simUI.inputDialog(string initValue="", string label="Input value:", string title="")"""
        ...

    def insertComboboxItem(self) -> Tuple[Any, int, int, str, bool]:
        """simUI.insertComboboxItem(string handle, int id, int index, string text, bool suppressEvents=true)"""
        ...

    def insertTableColumn(self, ui: int, widget: int, index: int) -> None:
        """simUI.insertTableColumn(int ui, int widget, int index)"""
        ...

    def insertTableRow(self, ui: int, widget: int, index: int) -> None:
        """simUI.insertTableRow(int ui, int widget, int index)"""
        ...

    def isVisible(self, handle: str) -> bool:
        """bool visibility = simUI.isVisible(string handle)"""
        ...

    def msgBox(self, type: int, buttons: int, title: str, message: str) -> int:
        """int result = simUI.msgBox(int type, int buttons, string title, string message)"""
        ...

    def qtVersion(self) -> list:
        """int[] version = simUI.qtVersion()"""
        ...

    def removeComboboxItem(self) -> Tuple[Any, int, int, bool]:
        """simUI.removeComboboxItem(string handle, int id, int index, bool suppressEvents=true)"""
        ...

    def removeCurve(self, handle: str, id: int, name: str) -> None:
        """simUI.removeCurve(string handle, int id, string name)"""
        ...

    def removeScene3DNode(self, handle: str, id: int, nodeId: int) -> None:
        """simUI.removeScene3DNode(string handle, int id, int nodeId)"""
        ...

    def removeTableColumn(self, ui: int, widget: int, index: int) -> None:
        """simUI.removeTableColumn(int ui, int widget, int index)"""
        ...

    def removeTableRow(self, ui: int, widget: int, index: int) -> None:
        """simUI.removeTableRow(int ui, int widget, int index)"""
        ...

    def removeTreeItem(self) -> Tuple[Any, int, int, bool]:
        """simUI.removeTreeItem(string handle, int id, int item_id, bool suppressEvents=true)"""
        ...

    def replot(self, handle: str, id: int) -> None:
        """simUI.replot(string handle, int id)"""
        ...

    def rescaleAxes(self) -> Tuple[Any, int, str, bool]:
        """simUI.rescaleAxes(string handle, int id, string name, bool onlyEnlargeX=false, bool onlyEnlargeY=false)"""
        ...

    def rescaleAxesAll(self) -> Tuple[Any, int, bool]:
        """simUI.rescaleAxesAll(string handle, int id, bool onlyEnlargeX=false, bool onlyEnlargeY=false)"""
        ...

    def restoreState(self, handle: str, id: int, state: bytes) -> None:
        """simUI.restoreState(string handle, int id, buffer state)"""
        ...

    def saveState(self, handle: str, id: int) -> bytes:
        """buffer state = simUI.saveState(string handle, int id)"""
        ...

    def setButtonPressed(self, handle: str, id: int, pressed: bool) -> None:
        """simUI.setButtonPressed(string handle, int id, bool pressed)"""
        ...

    def setButtonText(self, handle: str, id: int, text: str) -> None:
        """simUI.setButtonText(string handle, int id, string text)"""
        ...

    def setCheckboxValue(self) -> Tuple[Any, int, int, bool]:
        """simUI.setCheckboxValue(string handle, int id, int value, bool suppressEvents=true)"""
        ...

    def setClipboardText(self, text: str) -> None:
        """simUI.setClipboardText(string text)"""
        ...

    def setColumnCount(self) -> Tuple[Any, int, int, bool]:
        """simUI.setColumnCount(string handle, int id, int count, bool suppressEvents=true)"""
        ...

    def setColumnHeaderText(self, handle: str, id: int, column: int, text: str) -> None:
        """simUI.setColumnHeaderText(string handle, int id, int column, string text)"""
        ...

    def setColumnWidth(self, handle: str, id: int, column: int, min_size: int, max_size: int) -> None:
        """simUI.setColumnWidth(string handle, int id, int column, int min_size, int max_size)"""
        ...

    def setComboboxItems(self) -> Tuple[Any, int, list, int, bool]:
        """simUI.setComboboxItems(string handle, int id, string[] items, int index, bool suppressEvents=true)"""
        ...

    def setComboboxSelectedIndex(self) -> Tuple[Any, int, int, bool]:
        """simUI.setComboboxSelectedIndex(string handle, int id, int index, bool suppressEvents=true)"""
        ...

    def setCurrentEditWidget(self, handle: str, id: int) -> None:
        """simUI.setCurrentEditWidget(string handle, int id)"""
        ...

    def setCurrentTab(self) -> Tuple[Any, int, int, bool]:
        """simUI.setCurrentTab(string handle, int id, int index, bool suppressEvents=true)"""
        ...

    def setEditValue(self) -> Tuple[Any, int, str, bool]:
        """simUI.setEditValue(string handle, int id, string value, bool suppressEvents=true)"""
        ...

    def setEnabled(self) -> Tuple[Any, int, bool, bool]:
        """simUI.setEnabled(string handle, int id, bool enabled, bool suppressEvents=true)"""
        ...

    def setImageData(self, handle: str, id: int, data: bytes, width: int, height: int) -> None:
        """simUI.setImageData(string handle, int id, buffer data, int width, int height)"""
        ...

    def setItem(self) -> Tuple[Any, int, int, int, str, bool]:
        """simUI.setItem(string handle, int id, int row, int column, string text, bool suppressEvents=true)"""
        ...

    def setItemEditable(self, handle: str, id: int, row: int, column: int, editable: bool) -> None:
        """simUI.setItemEditable(string handle, int id, int row, int column, bool editable)"""
        ...

    def setItemImage(self) -> Tuple[Any, int, int, int, str, int, int, bool]:
        """simUI.setItemImage(string handle, int id, int row, int column, string data, int width, int height, bool suppressEvents=true)"""
        ...

    def setItems(self) -> Tuple[Any, int, str, bool]:
        """simUI.setItems(string handle, int id, string data, bool suppressEvents=true)"""
        ...

    def setLabelText(self) -> Tuple[Any, int, str, bool]:
        """simUI.setLabelText(string handle, int id, string text, bool suppressEvents=true)"""
        ...

    def setLegendVisibility(self, handle: str, id: int, visible: bool) -> None:
        """simUI.setLegendVisibility(string handle, int id, bool visible)"""
        ...

    def setMouseOptions(self, handle: str, id: int, panX: bool, panY: bool, zoomX: bool, zoomY: bool) -> None:
        """simUI.setMouseOptions(string handle, int id, bool panX, bool panY, bool zoomX, bool zoomY)"""
        ...

    def setPlotLabels(self, handle: str, id: int, x: str, y: str) -> None:
        """simUI.setPlotLabels(string handle, int id, string x, string y)"""
        ...

    def setPlotRanges(self, handle: str, id: int, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
        """simUI.setPlotRanges(string handle, int id, float xmin, float xmax, float ymin, float ymax)"""
        ...

    def setPlotXLabel(self, handle: str, id: int, label: str) -> None:
        """simUI.setPlotXLabel(string handle, int id, string label)"""
        ...

    def setPlotXRange(self, handle: str, id: int, xmin: float, xmax: float) -> None:
        """simUI.setPlotXRange(string handle, int id, float xmin, float xmax)"""
        ...

    def setPlotYLabel(self, handle: str, id: int, label: str) -> None:
        """simUI.setPlotYLabel(string handle, int id, string label)"""
        ...

    def setPlotYRange(self, handle: str, id: int, ymin: float, ymax: float) -> None:
        """simUI.setPlotYRange(string handle, int id, float ymin, float ymax)"""
        ...

    def setPosition(self) -> Tuple[Any, int, int, bool]:
        """simUI.setPosition(string handle, int x, int y, bool suppressEvents=true)"""
        ...

    def setProgress(self, handle: str, id: int, value: int) -> None:
        """simUI.setProgress(string handle, int id, int value)"""
        ...

    def setProperties(self) -> Tuple[Any, int, list, list, list, list, list, list, list, bool]:
        """simUI.setProperties(string handle, int id, string[] pnames, string[] ptypes, string[] pvalues, int[] pflags, string[] pdisplayk, string[] pdisplayv, int[] icons, bool suppressEvents=true)"""
        ...

    def setPropertiesContextMenu(self, handle: str, id: int, keys: list, titles: list) -> None:
        """simUI.setPropertiesContextMenu(string handle, int id, string[] keys, string[] titles)"""
        ...

    def setPropertiesRows(self) -> Tuple[Any, int, list, list, list, list, list, list, list, list, bool]:
        """simUI.setPropertiesRows(string handle, int id, int[] rows, string[] pnames, string[] ptypes, string[] pvalues, int[] pflags, string[] pdisplayk, string[] pdisplayv, int[] icons, bool suppressEvents=true)"""
        ...

    def setPropertiesSelection(self) -> Tuple[Any, int, int, bool]:
        """simUI.setPropertiesSelection(string handle, int id, int row, bool suppressEvents=true)"""
        ...

    def setPropertiesState(self, handle: str, id: int, state: str) -> None:
        """simUI.setPropertiesState(string handle, int id, string state)"""
        ...

    def setRadiobuttonValue(self) -> Tuple[Any, int, int, bool]:
        """simUI.setRadiobuttonValue(string handle, int id, int value, bool suppressEvents=true)"""
        ...

    def setRowCount(self) -> Tuple[Any, int, int, bool]:
        """simUI.setRowCount(string handle, int id, int count, bool suppressEvents=true)"""
        ...

    def setRowHeaderText(self, handle: str, id: int, row: int, text: str) -> None:
        """simUI.setRowHeaderText(string handle, int id, int row, string text)"""
        ...

    def setRowHeight(self, handle: str, id: int, row: int, min_size: int, max_size: int) -> None:
        """simUI.setRowHeight(string handle, int id, int row, int min_size, int max_size)"""
        ...

    def setScene3DNodeEnabled(self, handle: str, id: int, nodeId: int, enabled: bool) -> None:
        """simUI.setScene3DNodeEnabled(string handle, int id, int nodeId, bool enabled)"""
        ...

    def setScene3DNodeFloatParam(self, handle: str, id: int, nodeId: int, paramName: str, value: float) -> None:
        """simUI.setScene3DNodeFloatParam(string handle, int id, int nodeId, string paramName, float value)"""
        ...

    def setScene3DNodeIntParam(self, handle: str, id: int, nodeId: int, paramName: str, value: int) -> None:
        """simUI.setScene3DNodeIntParam(string handle, int id, int nodeId, string paramName, int value)"""
        ...

    def setScene3DNodeParam(self, ui: int, widget: int, nodeId: int, paramName: str, paramValue: Any) -> None:
        """simUI.setScene3DNodeParam(int ui, int widget, int nodeId, string paramName, any paramValue)"""
        ...

    def setScene3DNodeStringParam(self, handle: str, id: int, nodeId: int, paramName: str, value: str) -> None:
        """simUI.setScene3DNodeStringParam(string handle, int id, int nodeId, string paramName, string value)"""
        ...

    def setScene3DNodeVector2Param(self, handle: str, id: int, nodeId: int, paramName: str, x: float, y: float) -> None:
        """simUI.setScene3DNodeVector2Param(string handle, int id, int nodeId, string paramName, float x, float y)"""
        ...

    def setScene3DNodeVector3Param(self, handle: str, id: int, nodeId: int, paramName: str, x: float, y: float, z: float) -> None:
        """simUI.setScene3DNodeVector3Param(string handle, int id, int nodeId, string paramName, float x, float y, float z)"""
        ...

    def setScene3DNodeVector4Param(self, handle: str, id: int, nodeId: int, paramName: str, x: float, y: float, z: float, w: float) -> None:
        """simUI.setScene3DNodeVector4Param(string handle, int id, int nodeId, string paramName, float x, float y, float z, float w)"""
        ...

    def setSize(self) -> Tuple[Any, int, int, bool]:
        """simUI.setSize(string handle, int w, int h, bool suppressEvents=true)"""
        ...

    def setSliderValue(self) -> Tuple[Any, int, int, bool]:
        """simUI.setSliderValue(string handle, int id, int value, bool suppressEvents=true)"""
        ...

    def setSpinboxValue(self) -> Tuple[Any, int, float, bool]:
        """simUI.setSpinboxValue(string handle, int id, float value, bool suppressEvents=true)"""
        ...

    def setStyleSheet(self, handle: str, id: int, styleSheet: str) -> None:
        """simUI.setStyleSheet(string handle, int id, string styleSheet)"""
        ...

    def setTableSelection(self) -> Tuple[Any, int, int, int, bool]:
        """simUI.setTableSelection(string handle, int id, int row, int column, bool suppressEvents=true)"""
        ...

    def setText(self) -> Tuple[Any, int, str, bool]:
        """simUI.setText(string handle, int id, string text, bool suppressEvents=true)"""
        ...

    def setTitle(self) -> Tuple[Any, str, bool]:
        """simUI.setTitle(string handle, string title, bool suppressEvents=true)"""
        ...

    def setTreeSelection(self) -> Tuple[Any, int, int, bool]:
        """simUI.setTreeSelection(string handle, int id, int item_id, bool suppressEvents=true)"""
        ...

    def setUrl(self, handle: str, id: int, url: str) -> None:
        """simUI.setUrl(string handle, int id, string url)"""
        ...

    def setWidgetVisibility(self, handle: str, id: int, visibility: bool) -> None:
        """simUI.setWidgetVisibility(string handle, int id, bool visibility)"""
        ...

    def setWindowEnabled(self) -> Tuple[Any, bool, bool]:
        """simUI.setWindowEnabled(string handle, bool enabled, bool suppressEvents=true)"""
        ...

    def show(self, handle: str) -> None:
        """simUI.show(string handle)"""
        ...

    def supportedImageFormats(self, separator: str = nil) -> Tuple[list, str]:
        """string[] formatList, string formatListStr = simUI.supportedImageFormats(string separator=nil)"""
        ...

    def svgLoadData(self, handle: str, id: int, data: str) -> None:
        """simUI.svgLoadData(string handle, int id, string data)"""
        ...

    def svgLoadFile(self, handle: str, id: int, file: str) -> None:
        """simUI.svgLoadFile(string handle, int id, string file)"""
        ...

    def updateTreeItemParent(self) -> Tuple[Any, int, int, int, bool]:
        """simUI.updateTreeItemParent(string handle, int id, int item_id, int parent_id, bool suppressEvents=true)"""
        ...

    def updateTreeItemText(self, handle: str, id: int, item_id: int, text: list) -> None:
        """simUI.updateTreeItemText(string handle, int id, int item_id, string[] text)"""
        ...


class simURDF:
    """API functions for the `simURDF` module."""

    # --- Functions ---
    def export(self) -> Tuple[Any, str, int]:
        """simURDF.export(int origModel, string fileName, int options=0)"""
        ...

    def import(self, urdf: str, options: int = 0, packageStrReplace: str = nil) -> Tuple[str, list]:
        """string robotName, int[] modelHandles = simURDF.import(string urdf, int options=0, string packageStrReplace=nil)"""
        ...

    def sendTF(self, modelHandle: int, fileName: str) -> None:
        """simURDF.sendTF(int modelHandle, string fileName)"""
        ...


class simURLDrop:
    """API functions for the `simURLDrop` module."""

    # --- Constants ---
    download_mode_buffer: int
    download_mode_file: int
    pluginHandle: int

    # --- Functions ---
    def getURL(self, url: str, mode: int = simurldrop_download_mode_buffer) -> str:
        """string dataOrFilename = simURLDrop.getURL(string url, int mode=simurldrop_download_mode_buffer)"""
        ...

    def openURL(self, url: str) -> None:
        """simURLDrop.openURL(string url)"""
        ...


class simVision:
    """API functions for the `simVision` module."""

    # --- Functions ---
    def addBuffer1ToWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.addBuffer1ToWorkImg(int visionSensorHandle)"""
        ...

    def addWorkImgToBuffer1(self, visionSensorHandle: int) -> None:
        """simVision.addWorkImgToBuffer1(int visionSensorHandle)"""
        ...

    def binaryWorkImg(self, visionSensorHandle: int, threshold: float, oneProportion: float, oneTol: float, xCenter: float, xCenterTol: float, yCenter: float, yCenterTol: float, orient: float, orientTol: float, roundness: float, enableTrigger: bool, overlayColor: Any = ..., arg13: Any, arg14: Any) -> Tuple[bool, bytes]:
        """bool trigger, buffer packedDataPacket = simVision.binaryWorkImg(int visionSensorHandle, float threshold, float oneProportion, float oneTol, float xCenter, float xCenterTol, float yCenter, float yCenterTol, float orient, float orientTol, float roundness, bool enableTrigger, float[3] overlayColor={1.0, 0.0, 1.0})"""
        ...

    def blobDetectionOnWorkImg(self, visionSensorHandle: int, threshold: float, minBlobSize: float, modifyWorkImage: bool, overlayColor: Any = ..., arg5: Any, arg6: Any) -> Tuple[bool, bytes]:
        """bool trigger, buffer packedDataPacket = simVision.blobDetectionOnWorkImg(int visionSensorHandle, float threshold, float minBlobSize, bool modifyWorkImage, float[3] overlayColor={1.0, 0.0, 1.0})"""
        ...

    def buffer1ToWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.buffer1ToWorkImg(int visionSensorHandle)"""
        ...

    def buffer2ToWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.buffer2ToWorkImg(int visionSensorHandle)"""
        ...

    def changedPixelsOnWorkImg(self, visionSensorHandle: int, threshold: float) -> Tuple[bool, bytes]:
        """bool trigger, buffer packedDataPacket = simVision.changedPixelsOnWorkImg(int visionSensorHandle, float threshold)"""
        ...

    def circularCutWorkImg(self, visionSensorHandle: int, radius: float, copyToBuffer1: bool) -> None:
        """simVision.circularCutWorkImg(int visionSensorHandle, float radius, bool copyToBuffer1)"""
        ...

    def colorSegmentationOnWorkImg(self, visionSensorHandle: int, maxColorColorDistance: float) -> None:
        """simVision.colorSegmentationOnWorkImg(int visionSensorHandle, float maxColorColorDistance)"""
        ...

    def coordinatesFromWorkImg(self, visionSensorHandle: int, xyPointCount: Any, evenlySpacedInAngularSpace: bool, returnColorData: bool = false) -> Tuple[bool, bytes, bytes]:
        """bool trigger, buffer packedDataPacket, buffer colorData = simVision.coordinatesFromWorkImg(int visionSensorHandle, int[2] xyPointCount, bool evenlySpacedInAngularSpace, bool returnColorData=false)"""
        ...

    def createVelodyneHDL64E(self, visionSensorHandles: Any, frequency: float, options: int = 0, pointSize: int = 2, coloring_closeFarDist: Any = ..., arg5: Any, displayScalingFactor: float = 1) -> int:
        """int velodyneHandle = simVision.createVelodyneHDL64E(int[4] visionSensorHandles, float frequency, int options=0, int pointSize=2, float[2] coloring_closeFarDist={1, 5}, float displayScalingFactor=1)"""
        ...

    def createVelodyneVPL16(self, visionSensorHandles: Any, frequency: float, options: int = 0, pointSize: int = 2, coloring_closeFarDist: Any = ..., arg5: Any, displayScalingFactor: float = 1) -> int:
        """int velodyneHandle = simVision.createVelodyneVPL16(int[4] visionSensorHandles, float frequency, int options=0, int pointSize=2, float[2] coloring_closeFarDist={1, 5}, float displayScalingFactor=1)"""
        ...

    def destroyVelodyneHDL64E(self, velodyneHandle: int) -> int:
        """int result = simVision.destroyVelodyneHDL64E(int velodyneHandle)"""
        ...

    def destroyVelodyneVPL16(self, velodyneHandle: int) -> int:
        """int result = simVision.destroyVelodyneVPL16(int velodyneHandle)"""
        ...

    def distort(self) -> Tuple[Any, list]:
        """simVision.distort(int visionSensorHandle, int[] pixelMap=nil, float[] depthScalings=nil)"""
        ...

    def edgeDetectionOnWorkImg(self, visionSensorHandle: int, threshold: float) -> None:
        """simVision.edgeDetectionOnWorkImg(int visionSensorHandle, float threshold)"""
        ...

    def handleAnaglyphStereo(self, passiveVisionSensorHandle: int, activeVisionSensorHandles: Any, leftAndRightColors: Any = nil) -> int:
        """int result = simVision.handleAnaglyphStereo(int passiveVisionSensorHandle, int[2] activeVisionSensorHandles, float[6] leftAndRightColors=nil)"""
        ...

    def handleSpherical(self, passiveVisionSensorHandleForRGB: int, activeVisionSensorHandles: Any, horizontalAngle: float, verticalAngle: float, passiveVisionSensorHandleForDepth: int = -1) -> int:
        """int result = simVision.handleSpherical(int passiveVisionSensorHandleForRGB, int[6] activeVisionSensorHandles, float horizontalAngle, float verticalAngle, int passiveVisionSensorHandleForDepth=-1)"""
        ...

    def handleVelodyneHDL64E(self, velodyneHandle: int, dt: float) -> Tuple[bytes, bytes]:
        """buffer points, buffer colorData = simVision.handleVelodyneHDL64E(int velodyneHandle, float dt)"""
        ...

    def handleVelodyneVPL16(self, velodyneHandle: int, dt: float) -> Tuple[bytes, bytes]:
        """buffer points, buffer colorData = simVision.handleVelodyneVPL16(int velodyneHandle, float dt)"""
        ...

    def horizontalFlipWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.horizontalFlipWorkImg(int visionSensorHandle)"""
        ...

    def intensityScaleOnWorkImg(self, visionSensorHandle: int, start: float, end: float, greyScale: bool) -> None:
        """simVision.intensityScaleOnWorkImg(int visionSensorHandle, float start, float end, bool greyScale)"""
        ...

    def matrix3x3OnWorkImg(self) -> Tuple[Any, int, float, Any]:
        """simVision.matrix3x3OnWorkImg(int visionSensorHandle, int passes, float multiplier, float[9] matrix=nil)"""
        ...

    def matrix5x5OnWorkImg(self) -> Tuple[Any, int, float, Any]:
        """simVision.matrix5x5OnWorkImg(int visionSensorHandle, int passes, float multiplier, float[25] matrix=nil)"""
        ...

    def multiplyWorkImgWithBuffer1(self, visionSensorHandle: int) -> None:
        """simVision.multiplyWorkImgWithBuffer1(int visionSensorHandle)"""
        ...

    def normalizeWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.normalizeWorkImg(int visionSensorHandle)"""
        ...

    def rectangularCutWorkImg(self, visionSensorHandle: int, sizes: Any, copyToBuffer1: bool) -> None:
        """simVision.rectangularCutWorkImg(int visionSensorHandle, float[2] sizes, bool copyToBuffer1)"""
        ...

    def resizeWorkImg(self, visionSensorHandle: int, scaling: Any) -> None:
        """simVision.resizeWorkImg(int visionSensorHandle, float[2] scaling)"""
        ...

    def rotateWorkImg(self, visionSensorHandle: int, rotationAngle: float) -> None:
        """simVision.rotateWorkImg(int visionSensorHandle, float rotationAngle)"""
        ...

    def scaleAndOffsetWorkImg(self, visionSensorHandle: int, preOffset: Any, scaling: Any, postOffset: Any, rgb: bool) -> None:
        """simVision.scaleAndOffsetWorkImg(int visionSensorHandle, float[3] preOffset, float[3] scaling, float[3] postOffset, bool rgb)"""
        ...

    def selectiveColorOnWorkImg(self, visionSensorHandle: int, color: Any, colorTolerance: Any, rgb: bool, keep: bool, removedPartToBuffer1: bool) -> None:
        """simVision.selectiveColorOnWorkImg(int visionSensorHandle, float[3] color, float[3] colorTolerance, bool rgb, bool keep, bool removedPartToBuffer1)"""
        ...

    def sensorDepthMapToWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.sensorDepthMapToWorkImg(int visionSensorHandle)"""
        ...

    def sensorImgToWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.sensorImgToWorkImg(int visionSensorHandle)"""
        ...

    def sharpenWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.sharpenWorkImg(int visionSensorHandle)"""
        ...

    def shiftWorkImg(self, visionSensorHandle: int, shift: Any, wrapAround: bool) -> None:
        """simVision.shiftWorkImg(int visionSensorHandle, float[2] shift, bool wrapAround)"""
        ...

    def subtractBuffer1FromWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.subtractBuffer1FromWorkImg(int visionSensorHandle)"""
        ...

    def subtractWorkImgFromBuffer1(self, visionSensorHandle: int) -> None:
        """simVision.subtractWorkImgFromBuffer1(int visionSensorHandle)"""
        ...

    def swapBuffers(self, visionSensorHandle: int) -> None:
        """simVision.swapBuffers(int visionSensorHandle)"""
        ...

    def swapWorkImgWithBuffer1(self, visionSensorHandle: int) -> None:
        """simVision.swapWorkImgWithBuffer1(int visionSensorHandle)"""
        ...

    def uniformImgToWorkImg(self, visionSensorHandle: int, color: Any) -> None:
        """simVision.uniformImgToWorkImg(int visionSensorHandle, float[3] color)"""
        ...

    def velodyneDataFromWorkImg(self, visionSensorHandle: int, xyPointCount: Any, vAngle: float, returnColorData: bool = false) -> Tuple[bool, bytes, bytes]:
        """bool trigger, buffer packedDataPacket, buffer colorData = simVision.velodyneDataFromWorkImg(int visionSensorHandle, int[2] xyPointCount, float vAngle, bool returnColorData=false)"""
        ...

    def verticalFlipWorkImg(self, visionSensorHandle: int) -> None:
        """simVision.verticalFlipWorkImg(int visionSensorHandle)"""
        ...

    def workImgToBuffer1(self, visionSensorHandle: int) -> None:
        """simVision.workImgToBuffer1(int visionSensorHandle)"""
        ...

    def workImgToBuffer2(self, visionSensorHandle: int) -> None:
        """simVision.workImgToBuffer2(int visionSensorHandle)"""
        ...

    def workImgToSensorDepthMap(self) -> Tuple[Any, bool]:
        """simVision.workImgToSensorDepthMap(int visionSensorHandle, bool removeBuffer=true)"""
        ...

    def workImgToSensorImg(self) -> Tuple[Any, bool]:
        """simVision.workImgToSensorImg(int visionSensorHandle, bool removeBuffer=true)"""
        ...


class simWS:
    """API functions for the `simWS` module."""

    # --- Constants ---
    opcode_binary: int
    opcode_continuation: int
    opcode_text: int
    pluginHandle: int

    # --- Functions ---
    def connect(self, uri: str) -> str:
        """string clientHandle = simWS.connect(string uri)"""
        ...

    def disconnect(self, clientHandle: str) -> None:
        """simWS.disconnect(string clientHandle)"""
        ...

    def send(self) -> Tuple[Any, str, bytes, int]:
        """simWS.send(string serverOrClientHandle, string connectionHandle, buffer data, int opcode=simws_opcode_text)"""
        ...

    def setCloseHandler(self, serverOrClientHandle: str, callbackFn: str) -> None:
        """simWS.setCloseHandler(string serverOrClientHandle, string callbackFn)"""
        ...

    def setFailHandler(self, serverOrClientHandle: str, callbackFn: str) -> None:
        """simWS.setFailHandler(string serverOrClientHandle, string callbackFn)"""
        ...

    def setHTTPHandler(self, serverHandle: str, callbackFn: str) -> None:
        """simWS.setHTTPHandler(string serverHandle, string callbackFn)"""
        ...

    def setMessageHandler(self, serverOrClientHandle: str, callbackFn: str) -> None:
        """simWS.setMessageHandler(string serverOrClientHandle, string callbackFn)"""
        ...

    def setOpenHandler(self, serverOrClientHandle: str, callbackFn: str) -> None:
        """simWS.setOpenHandler(string serverOrClientHandle, string callbackFn)"""
        ...

    def start(self, listenPort: int) -> str:
        """string serverHandle = simWS.start(int listenPort)"""
        ...

    def stop(self, serverHandle: str) -> None:
        """simWS.stop(string serverHandle)"""
        ...


class simZMQ:
    """API functions for the `simZMQ` module."""

    # --- Functions ---
    def bind(self, socket: str, endpoint: str) -> int:
        """int result = simZMQ.bind(string socket, string endpoint)"""
        ...

    def close(self, socket: str) -> int:
        """int result = simZMQ.close(string socket)"""
        ...

    def connect(self, socket: str, endpoint: str) -> int:
        """int result = simZMQ.connect(string socket, string endpoint)"""
        ...

    def connect_peer(self, socket: str, addr: str) -> int:
        """int result = simZMQ.connect_peer(string socket, string addr)"""
        ...

    def ctx_get(self, context: str, option_name: int) -> int:
        """int result = simZMQ.ctx_get(string context, int option_name)"""
        ...

    def ctx_get_ext(self, context: str, option_name: int) -> Tuple[int, bytes]:
        """int result, buffer data = simZMQ.ctx_get_ext(string context, int option_name)"""
        ...

    def ctx_new(self) -> str:
        """string context = simZMQ.ctx_new()"""
        ...

    def ctx_set(self, context: str, option_name: int, option_value: int) -> int:
        """int result = simZMQ.ctx_set(string context, int option_name, int option_value)"""
        ...

    def ctx_set_ext(self, context: str, option_name: int, option_value: bytes) -> int:
        """int result = simZMQ.ctx_set_ext(string context, int option_name, buffer option_value)"""
        ...

    def ctx_shutdown(self, context: str) -> int:
        """int result = simZMQ.ctx_shutdown(string context)"""
        ...

    def ctx_singleton(self) -> str:
        """string context = simZMQ.ctx_singleton()"""
        ...

    def ctx_term(self, context: str) -> int:
        """int result = simZMQ.ctx_term(string context)"""
        ...

    def disconnect(self, socket: str, endpoint: str) -> int:
        """int result = simZMQ.disconnect(string socket, string endpoint)"""
        ...

    def errnum(self) -> int:
        """int result = simZMQ.errnum()"""
        ...

    def getsockopt(self, socket: str, option_name: int, option_len: int) -> Tuple[int, bytes]:
        """int result, buffer value = simZMQ.getsockopt(string socket, int option_name, int option_len)"""
        ...

    def has(self, capability: str) -> int:
        """int result = simZMQ.has(string capability)"""
        ...

    def join(self, socket: str, group: str) -> int:
        """int result = simZMQ.join(string socket, string group)"""
        ...

    def leave(self, socket: str, group: str) -> int:
        """int result = simZMQ.leave(string socket, string group)"""
        ...

    def msg_close(self, msg: str) -> int:
        """int result = simZMQ.msg_close(string msg)"""
        ...

    def msg_copy(self, dest: str, src: str) -> int:
        """int result = simZMQ.msg_copy(string dest, string src)"""
        ...

    def msg_data(self, msg: str) -> bytes:
        """buffer data = simZMQ.msg_data(string msg)"""
        ...

    def msg_destroy(self, msg: str) -> None:
        """simZMQ.msg_destroy(string msg)"""
        ...

    def msg_get(self, msg: str, property: int) -> int:
        """int result = simZMQ.msg_get(string msg, int property)"""
        ...

    def msg_gets(self, msg: str, property: str) -> Tuple[int, str]:
        """int result, string value = simZMQ.msg_gets(string msg, string property)"""
        ...

    def msg_group(self, msg: str) -> Tuple[int, str]:
        """int result, string group = simZMQ.msg_group(string msg)"""
        ...

    def msg_init(self, msg: str) -> int:
        """int result = simZMQ.msg_init(string msg)"""
        ...

    def msg_init_size(self, msg: str, size: int) -> int:
        """int result = simZMQ.msg_init_size(string msg, int size)"""
        ...

    def msg_more(self, msg: str) -> int:
        """int result = simZMQ.msg_more(string msg)"""
        ...

    def msg_move(self, dest: str, src: str) -> int:
        """int result = simZMQ.msg_move(string dest, string src)"""
        ...

    def msg_new(self) -> str:
        """string msg = simZMQ.msg_new()"""
        ...

    def msg_recv(self, msg: str, socket: str, flags: int) -> int:
        """int result = simZMQ.msg_recv(string msg, string socket, int flags)"""
        ...

    def msg_routing_id(self, msg: str) -> int:
        """int routing_id = simZMQ.msg_routing_id(string msg)"""
        ...

    def msg_send(self, msg: str, socket: str, flags: int) -> int:
        """int result = simZMQ.msg_send(string msg, string socket, int flags)"""
        ...

    def msg_set(self, msg: str, property: int, value: int) -> int:
        """int result = simZMQ.msg_set(string msg, int property, int value)"""
        ...

    def msg_set_group(self, msg: str, group: str) -> int:
        """int result = simZMQ.msg_set_group(string msg, string group)"""
        ...

    def msg_set_routing_id(self, msg: str, routing_id: int) -> int:
        """int result = simZMQ.msg_set_routing_id(string msg, int routing_id)"""
        ...

    def msg_size(self, msg: str) -> int:
        """int result = simZMQ.msg_size(string msg)"""
        ...

    def poll(self, sockets: list, events: list, timeout: int = 0) -> Tuple[int, list]:
        """int result, int[] revents = simZMQ.poll(string[] sockets, int[] events, int timeout=0)"""
        ...

    def proxy(self, frontend: str, backend: str, capture: str) -> int:
        """int result = simZMQ.proxy(string frontend, string backend, string capture)"""
        ...

    def proxy_steerable(self, frontend: str, backend: str, capture: str, control: str) -> int:
        """int result = simZMQ.proxy_steerable(string frontend, string backend, string capture, string control)"""
        ...

    def recv(self, socket: str, flags: int, max_buf_size: int = nil) -> Tuple[int, bytes]:
        """int result, buffer data = simZMQ.recv(string socket, int flags, int max_buf_size=nil)"""
        ...

    def send(self, socket: str, data: bytes, flags: int) -> int:
        """int result = simZMQ.send(string socket, buffer data, int flags)"""
        ...

    def setsockopt(self, socket: str, option_name: int, option_value: bytes) -> int:
        """int result = simZMQ.setsockopt(string socket, int option_name, buffer option_value)"""
        ...

    def socket(self, context: str, type: int) -> str:
        """string socket = simZMQ.socket(string context, int type)"""
        ...

    def socket_monitor(self, socket: str, endpoint: str, events: int) -> int:
        """int result = simZMQ.socket_monitor(string socket, string endpoint, int events)"""
        ...

    def strerror(self, errnum: int) -> str:
        """string message = simZMQ.strerror(int errnum)"""
        ...

    def unbind(self, socket: str, endpoint: str) -> int:
        """int result = simZMQ.unbind(string socket, string endpoint)"""
        ...

    def version(self) -> Tuple[int, int, int]:
        """int major, int minor, int patch = simZMQ.version()"""
        ...


# --- API instances for autocompletion ---
base16: base16
base64: base64
checkarg: checkarg
io: io
itertools: itertools
operator: operator
sim: sim
simAssimp: simAssimp
simBWF: simBWF
simBubble: simBubble
simCHAI3D: simCHAI3D
simCam: simCam
simCmd: simCmd
simConvex: simConvex
simEigen: simEigen
simEvents: simEvents
simGLTF: simGLTF
simGeom: simGeom
simICP: simICP
simIGL: simIGL
simIK: simIK
simIM: simIM
simLDraw: simLDraw
simMIDI: simMIDI
simMTB: simMTB
simMujoco: simMujoco
simOMPL: simOMPL
simOpenMesh: simOpenMesh
simPython: simPython
simQML: simQML
simROS2: simROS2
simRRS1: simRRS1
simRemoteApi: simRemoteApi
simSDF: simSDF
simSubprocess: simSubprocess
simSurfRec: simSurfRec
simUI: simUI
simURDF: simURDF
simURLDrop: simURLDrop
simVision: simVision
simWS: simWS
simZMQ: simZMQ
