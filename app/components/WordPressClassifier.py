from app.components.Classifier import Classifier


class WordPressClassifier(Classifier):
    classifier = []
    log = None

    def __init__(self):
        self.classifier = [
            {
                'label': 'internal',
                'level': 0,
                'checks': [
                    [['uri', 'is', '/wp-cron.php'], ['method', 'in', ['GET', 'POST']]]
                ]
            },
            {
                'label': 'service',
                'level': 1,
                'checks': [
                    [['uri', 'is', '/wp-sentry.php'], ['method', 'is', 'POST']],
                    [['uri', 'is', '/'], ['get', 'contains', 'wordfence_syncAttackData']],
                    [['uri', 'is', '/'], ['get', 'contains', ['_wfsf', 'detectProxy']]],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', 'wordfence_testAjax'], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', 'wordfence_doScan'], ['method', 'is', 'GET']],
                ]
            },
            {
                'label': 'traffic',
                'level': 2,
                'checks': [
                    [['uri', 'is', '/'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'is', '//'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'is', '///'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'is', '/wp-admin/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/index.php'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/favicon.ico'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/favicon.png'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/robots.txt'], ['method', 'is', 'GET']],
                    [['uri', 'contains', 'sitemap.xml'], ['method', 'is', 'GET']],
                    [['uri', 'contains', 'sitemap_index.xml'], ['method', 'is', 'GET']],
                    [['uri', 'in', ['/feed', '/feed/', '/atom', '/feed/atom/']], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/wordpress-plugins/'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'startsWith', '/page/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/blog/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/thanks-for-the-tip/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/about'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'startsWith', '/thoughts'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/comments/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/2018/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/2017/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/2016/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/2012/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/2004/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/category/'], ['method', 'in', ['GET', 'HEAD']]],
                    [['uri', 'startsWith', '/tag/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/author/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/snippets/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/type/video/'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/wp-login.php'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/rss'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/wp-json/oembed/1.0/embed'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/wp-json/contact-form-7/v1/contact-forms/36/feedback'], ['method', 'is', 'POST']]
                ]
            },
            {
                'label': 'probe',
                'level': 3,
                'checks': [
                    [['uri', 'is', '/wordpress/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/admin/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/wp/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/new/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/old/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/test/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/main/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/site/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/backup/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/demo/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/home/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/temp/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/tmp/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/cms/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/dev/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/portal/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/web/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/profile/register'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/join'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/wp-json/'], ['method', 'is', 'GET']],
                    [['uri', 'is', '/user/register'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', 'vuln.htm'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'is', '[]'], ['post', 'is', '[]']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', 'cp_add_subscriber']],
                    [['uri', 'endsWith', '.txt'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '.zip'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '.sql'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '.gz'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '.dat'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '.suspected'], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['/plugins', '.css']], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['/plugins', '.js']], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['/plugins', '.txt']], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['/plugins', '.jpg']], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['/plugins', '.gif']], ['method', 'is', 'GET']],
                    [['uri', 'contains', '/setup-config.php'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/xmlrpc.php'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/wp-json/siteground-optimizer/'], ['get', 'is', '[]'], ['post', 'is', '[]'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/wp-json/siteground-optimizer/'], ['get', 'is', '[]'], ['post', 'is', '[]'], ['method', 'is', 'POST']],
                    [['uri', 'startsWith', '/0manager/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/admin/'], ['uri', 'endsWith', '.gif'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/templates/'], ['uri', 'endsWith', '.css'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/wp-json/wp/v2/posts/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/wp-json/wp/v2/posts/'], ['uri', 'contains', ['href', 'revisions', 'attachment', 'media']], ['method', 'is', 'GET']],
                    [['uri', 'contains', '/admin/fckeditor'], ['uri', 'endsWith', 'uploadtest.html'], ['method', 'is', 'GET']],
                    [['uri', 'contain', 'FCKeditor/editor'], ['uri', 'endsWith', 'uploadtest.html'], ['method', 'is', 'GET']],
                    [['uri', 'contain', 'struts2-showcase'], ['method', 'is', 'GET']]
                ]
            },
            {
                'label': 'suspicious',
                'level': 4,
                'checks': [
                    [['get', 'contains', ['gf_page', 'upload']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', 'maint/repair.php'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', 'xmlrpc.php'], ['get', 'is', '[]'], ['post', 'is', '[]'], ['method', 'is', 'POST']],
                    [['method', 'is', 'POST'], ['get', 'is', '[]'], ['post', 'is', '[]']]
                ]
            },
            {
                'label': 'attempts',
                'level': 5,
                'checks': [
                    [['uri', 'contains', '/wp-json/wp/v2/users/'], ['method', 'is', 'GET']],
                    [['uri', 'startsWith', '/0admin'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/wp-login.php'], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/xmlrpc.php'], ['post', 'contains', 'wp.getUsersBlogs']],
                    [['uri', 'endsWith', '/xmlrpc.php'], ['post', 'contains', 'pingback.ping']],
                    [['uri', 'contains', ['wp-config', 'backup']], ['method', 'is', 'GET']],
                    [['uri', 'contains', ['wp-config', 'bak']], ['method', 'is', 'GET']],
                ]
            },
            {
                'label': 'hostile',
                'level': 6,
                'checks': [
                    [['post', 'contains', 'die('], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['wpgdprc_process_action', 'users_can_register']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['kiwi_social_share_set_option', 'users_can_register']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['td_ajax_update_panel', 'users_can_register']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['td_mod_register', 'email', 'user']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['cp_add_subscriber', 'cp_set_user', 'administrator']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['wysija_campaigns', 'action', 'themes']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['wysija_campaigns', 'action', 'themes']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', 'wpuf_file_upload'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'is', '[]'], ['post', 'is', '[]'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['getcountryuser', 'cs']], ['method', 'is', 'GET']],
                    [['uri', 'is', '/jm-ajax/upload_file/'], ['get', 'is', '[]'], ['post', 'is', '[]'], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['post', 'contains', ['String.fromCharCode']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['String.fromCharCode']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['String.fromCharCode']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['String.fromCharCode']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['yp_remote_get']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'css']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'css']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'js']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'js']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['yp_remote_get']], ['post', 'contains', ['yp_json_import_data', 'home']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['action', 'update_zb_fbc_code']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['Action', 'EWD_UFAQ_UpdateOptions']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['Action', 'EWD_UFAQ_UpdateOptions']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['swpsmtp_import_settings', '1']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['post', 'contains', ['swpsmtp_import_settings', '1']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'wpgdprc_process_action', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'wpgdprc_process_action', 'home']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'td_ajax_update_panel', 'wp_option', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'td_ajax_update_panel', 'wp_option', 'home']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['thim_update_theme_mods', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['thim_update_theme_mods', 'home']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-post.php'], ['post', 'contains', ['wuev_form_type', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['miglaA_update_me', 'siteurl']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['miglaA_update_me', 'home']], ['method', 'is', 'POST']],
                    [['post', 'contains', 'String.fromCharCode']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['get', 'contains', ['action', 'wcp_change_post_width']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['page', 'yuzo-related-post']], ['method', 'is', 'GET']],
                    [['uri', 'endsWith', '/admin-post.php'], ['get', 'contains', ['action', 'save', 'updated', 'true']], ['method', 'is', 'GET']],
                    [['uri', 'contains', 'vendor/phpunit']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'wpgdprc_process_action', 'security', '""']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'um_fileupload']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'um_remove_file']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'td_ajax_search']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'kiwi_social_share_get_option', 'args', 'group', 'cron']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'thim_login_ajax']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'wpsp_upload_attachment']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'get_currentRef', 'formID']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'mk_file_folder_manager']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'cs_employer_ajax_profile', 'cs_uid']], ['method', 'is', 'POST']],
                    [['uri', 'is', '/'], ['post', 'contains', ['action', 'update', 'profile', 'image', 'sub_action', 'upload_avatar']], ['method', 'is', 'POST']],
                    [['uri', 'endsWith', '/admin-ajax.php'], ['post', 'contains', ['action', 'migla_getme', 'key', 'cron']], ['method', 'is', 'POST']],
                ]
            }
        ]
