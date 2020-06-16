# -*- coding: utf_8 -*-
import logging
import json
import os
import shutil

from django.conf import settings
from django.db.models import QuerySet
from django.conf import settings
from Kensa.utils import python_dict, python_list

from StaticAnalyzer.models import StaticAnalyzerAndroid
from StaticAnalyzer.models import RecentScansDB

"""Module holding the functions for the db."""


logger = logging.getLogger(__name__)


def get_context_from_db_entry(db_entry: QuerySet) -> dict:
    """Return the context for APK/ZIP from DB."""
    try:
        logger.info('Analysis is already Done. Fetching data from the DB...')
        context = {
            'version': settings.KENSA_VER,
            'title': 'Static Analysis',
            'file_name': db_entry[0].FILE_NAME,
            'app_name': db_entry[0].APP_NAME,
            'app_type': db_entry[0].APP_TYPE,
            'size': db_entry[0].SIZE,
            'md5': db_entry[0].MD5,
            'sha1': db_entry[0].SHA1,
            'sha256': db_entry[0].SHA256,
            'package_name': db_entry[0].PACKAGE_NAME,
            'main_activity': db_entry[0].MAIN_ACTIVITY,
            'exported_activities': db_entry[0].EXPORTED_ACTIVITIES,
            'browsable_activities': python_dict(
                db_entry[0].BROWSABLE_ACTIVITIES),
            'activities': python_list(db_entry[0].ACTIVITIES),
            'receivers': python_list(db_entry[0].RECEIVERS),
            'providers': python_list(db_entry[0].PROVIDERS),
            'services': python_list(db_entry[0].SERVICES),
            'libraries': python_list(db_entry[0].LIBRARIES),
            'target_sdk': db_entry[0].TARGET_SDK,
            'max_sdk': db_entry[0].MAX_SDK,
            'min_sdk': db_entry[0].MIN_SDK,
            'version_name': db_entry[0].VERSION_NAME,
            'version_code': db_entry[0].VERSION_CODE,
            'icon_hidden': db_entry[0].ICON_HIDDEN,
            'icon_found': db_entry[0].ICON_FOUND,
            'permissions': python_dict(db_entry[0].PERMISSIONS),
            'certificate_analysis': python_dict(
                db_entry[0].CERTIFICATE_ANALYSIS),
            'manifest_analysis': python_list(db_entry[0].MANIFEST_ANALYSIS),
            'binary_analysis': python_list(db_entry[0].BINARY_ANALYSIS),
            'file_analysis': python_list(db_entry[0].FILE_ANALYSIS),
            'android_api': python_dict(db_entry[0].ANDROID_API),
            'code_analysis': python_dict(db_entry[0].CODE_ANALYSIS),
            'urls': python_list(db_entry[0].URLS),
            'domains': python_dict(db_entry[0].DOMAINS),
            'emails': python_list(db_entry[0].EMAILS),
            'strings': python_list(db_entry[0].STRINGS),
            'firebase_urls': python_list(db_entry[0].FIREBASE_URLS),
            'files': python_list(db_entry[0].FILES),
            'exported_count': python_dict(db_entry[0].EXPORTED_COUNT),
            'apkid': python_dict(db_entry[0].APKID),
            'trackers': python_dict(db_entry[0].TRACKERS),
            'playstore_details': python_dict(db_entry[0].PLAYSTORE_DETAILS),
        }
        return context
    except Exception:
        logger.exception('Fetching from DB')

def get_android_context(static_db)->dict:
    """Return the context for APK/ZIP from DB."""
    try:
        logger.info('Analysis is already Done. Fetching data from the DB...')
        context = {
            'version': settings.KENSA_VER,
            'title': 'Static Analysis',
            'file_name': static_db.FILE_NAME,
            'app_name': static_db.APP_NAME,
            'app_type': static_db.APP_TYPE,
            'size': static_db.SIZE,
            'md5': static_db.MD5,
            'sha1': static_db.SHA1,
            'sha256': static_db.SHA256,
            'package_name': static_db.PACKAGE_NAME,
            'main_activity': static_db.MAIN_ACTIVITY,
            'exported_activities': static_db.EXPORTED_ACTIVITIES,
            'browsable_activities': python_dict(
                static_db.BROWSABLE_ACTIVITIES),
            'activities': python_list(static_db.ACTIVITIES),
            'receivers': python_list(static_db.RECEIVERS),
            'providers': python_list(static_db.PROVIDERS),
            'services': python_list(static_db.SERVICES),
            'libraries': python_list(static_db.LIBRARIES),
            'target_sdk': static_db.TARGET_SDK,
            'max_sdk': static_db.MAX_SDK,
            'min_sdk': static_db.MIN_SDK,
            'version_name': static_db.VERSION_NAME,
            'version_code': static_db.VERSION_CODE,
            'icon_hidden': static_db.ICON_HIDDEN,
            'icon_found': static_db.ICON_FOUND,
            'permissions': python_dict(static_db.PERMISSIONS),
            'certificate_analysis': python_dict(
                static_db.CERTIFICATE_ANALYSIS),
            'manifest_analysis': python_list(static_db.MANIFEST_ANALYSIS),
            'binary_analysis': python_list(static_db.BINARY_ANALYSIS),
            'file_analysis': python_list(static_db.FILE_ANALYSIS),
            'android_api': python_dict(static_db.ANDROID_API),
            'code_analysis': python_dict(static_db.CODE_ANALYSIS),
            'urls': python_list(static_db.URLS),
            'domains': python_dict(static_db.DOMAINS),
            'emails': python_list(static_db.EMAILS),
            'strings': python_list(static_db.STRINGS),
            'firebase_urls': python_list(static_db.FIREBASE_URLS),
            'files': python_list(static_db.FILES),
            'exported_count': python_dict(static_db.EXPORTED_COUNT),
            'apkid': python_dict(static_db.APKID),
            'trackers': python_dict(static_db.TRACKERS),
            'playstore_details': python_dict(static_db.PLAYSTORE_DETAILS),
        }
        return context
    except Exception:
        logger.exception('Fetching from DB')

def get_context_from_analysis(app_dic,
                              man_data_dic,
                              man_an_dic,
                              code_an_dic,
                              cert_dic,
                              bin_anal,
                              apk_id,
                              trackers) -> dict:
    """Get the context for APK/ZIP from analysis results."""
    try:
        context = {
            'title': 'Static Analysis',
            'version': settings.KENSA_VER,
            'file_name': app_dic['app_name'],
            'app_name': app_dic['real_name'],
            'app_type': app_dic['zipped'],
            'size': app_dic['size'],
            'md5': app_dic['md5'],
            'sha1': app_dic['sha1'],
            'sha256': app_dic['sha256'],
            'package_name': man_data_dic['packagename'],
            'main_activity': man_data_dic['mainactivity'],
            'exported_activities': man_an_dic['exported_act'],
            'browsable_activities': man_an_dic['browsable_activities'],
            'activities': man_data_dic['activities'],
            'receivers': man_data_dic['receivers'],
            'providers': man_data_dic['providers'],
            'services': man_data_dic['services'],
            'libraries': man_data_dic['libraries'],
            'target_sdk': man_data_dic['target_sdk'],
            'max_sdk': man_data_dic['max_sdk'],
            'min_sdk': man_data_dic['min_sdk'],
            'version_name': man_data_dic['androvername'],
            'version_code': man_data_dic['androver'],
            'icon_hidden': app_dic['icon_hidden'],
            'icon_found': app_dic['icon_found'],
            'certificate_analysis': cert_dic,
            'permissions': man_an_dic['permissons'],
            'manifest_analysis': man_an_dic['manifest_anal'],
            'binary_analysis': bin_anal,
            'file_analysis': app_dic['certz'],
            'android_api': code_an_dic['api'],
            'code_analysis': code_an_dic['findings'],
            'urls': code_an_dic['urls'],
            'domains': code_an_dic['domains'],
            'emails': code_an_dic['emails'],
            'strings': app_dic['strings'],
            'firebase_urls': code_an_dic['firebase'],
            'files': app_dic['files'],
            'exported_count': man_an_dic['exported_cnt'],
            'apkid': apk_id,
            'trackers': trackers,
            'playstore_details': app_dic['playstore'],
        }
        return context
    except Exception:
        logger.exception('Rendering to Template')


def save_or_update(update_type,
                   app_dic,
                   man_data_dic,
                   man_an_dic,
                   code_an_dic,
                   cert_dic,
                   bin_anal,
                   apk_id,
                   trackers,
                   user,
                   organization):
    """
    Save/Update an APK/ZIP DB entry.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    try:
        values = { 
            'FILE_NAME': app_dic['app_name'],
            'APP_NAME': app_dic['real_name'],
            'APP_TYPE': app_dic['zipped'],
            'SIZE': app_dic['size'],
            'MD5': app_dic['md5'],
            'SHA1': app_dic['sha1'],
            'SHA256': app_dic['sha256'],
            'PACKAGE_NAME': man_data_dic['packagename'],
            'MAIN_ACTIVITY': man_data_dic['mainactivity'],
            'EXPORTED_ACTIVITIES': man_an_dic['exported_act'],
            'BROWSABLE_ACTIVITIES': man_an_dic['browsable_activities'],
            'ACTIVITIES': man_data_dic['activities'],
            'RECEIVERS': man_data_dic['receivers'],
            'PROVIDERS': man_data_dic['providers'],
            'SERVICES': man_data_dic['services'],
            'LIBRARIES': man_data_dic['libraries'],
            'TARGET_SDK': man_data_dic['target_sdk'],
            'MAX_SDK': man_data_dic['max_sdk'],
            'MIN_SDK': man_data_dic['min_sdk'],
            'VERSION_NAME': man_data_dic['androvername'],
            'VERSION_CODE': man_data_dic['androver'],
            'ICON_HIDDEN': app_dic['icon_hidden'],
            'ICON_FOUND': app_dic['icon_found'],
            'CERTIFICATE_ANALYSIS': cert_dic,
            'PERMISSIONS': man_an_dic['permissons'],
            'MANIFEST_ANALYSIS': man_an_dic['manifest_anal'],
            'BINARY_ANALYSIS': bin_anal,
            'FILE_ANALYSIS': app_dic['certz'],
            'ANDROID_API': code_an_dic['api'],
            'CODE_ANALYSIS': code_an_dic['findings'],
            'URLS': code_an_dic['urls'],
            'DOMAINS': code_an_dic['domains'],
            'EMAILS': code_an_dic['emails'],
            'STRINGS': app_dic['strings'],
            'FIREBASE_URLS': code_an_dic['firebase'],
            'FILES': app_dic['files'],
            'EXPORTED_COUNT': man_an_dic['exported_cnt'],
            'APKID': apk_id,
            'TRACKERS': trackers,
            'PLAYSTORE_DETAILS': app_dic['playstore'],
            "USER" : user,
            "ORGANIZATION" : organization
        }


        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # The code below handles the type of db interaction on flag
        # passed on by the static_analyzer_android function.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


        up_values = { # Update values for RecentScansDB
                'APP_NAME': app_dic['real_name'],
                'PACKAGE_NAME': man_data_dic['packagename'],
                'VERSION_NAME': man_data_dic['androvername'],
        }

        # [!] Do NOT edit below the line unless you know what you are doing.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if update_type == 'save':

            # Create new SSA entry
            logger.info("calling StaticAnalizerAndroid.objects.create")
            scan_obj = StaticAnalyzerAndroid.objects.create(**values)
            logger.info("Object %s saved" % (scan_obj.pk))


            # Update the RecentScansDB with the SSA data
            logger.info("updating RecentScansDB")
            RecentScansDB.objects.filter(MD5=app_dic['md5']).update(**up_values)
            logger.info("RecentScansDB entry %s updated" % app_dic["md5"])


            # Get the scan info for the response by pasing obj, not PK
            app_info = StaticAnalyzerAndroid.get_scan_info_from_obj(scan_obj)


            # If scan_info_from_obj returns None,
            if app_info is None:
                return {"error" : "error getting scan info from obj %s" % app_dic["md5"]}, 500
            else:
                return app_info, 200

            # Fallback.
            return {"error" : "android.db_interaction.save_or_update failed on creation."}, 500


        # This is an unpdate procedure, do NOT edit below the line unless you
        # know what you are doing.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:

            # Update SSA
            logger.info("updating StaticAnlaizerAndroid")
            StaticAnalyzerAndroid.objects.filter(MD5=app_dic['md5']).update(**values)
            logger.info("StaticAnalizerAndroid %s updated" % app_dic["md5"])

            # Update RecentScansDB
            logger.info("updating RecentScansDB")
            RecentScansDB.objects.filter(MD5=app_dic['md5']).update(**up_values)
            logger.info("RecentScansDB entry updated")

            # Getting data from object for controller, this bubbles all the way up
            # to the controller.
            logger.info("Getting scan_info_from_obj")
            context = StaticAnalyzerAndroid.get_scan_info_from_obj(
                StaticAnalyzerAndroid.objects.get(MD5=app_dic["md5"]))


        if context is not None:
            return context, 200


        return {"error" : "error getting scan info"}, 500


    # This is the fallback operation when a scan fails.
    # Do NOT edit below line unless you know what you are doing.
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 1) Remove RecentScansDB entry
    # 2) Remove any dirs and files associated with the failed scan.
    # 3) Return and error with resp 500. (bubbles up to the controller)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    except Exception as error:

        logger.error('android.db_interaction.save_or_update failed.')

        logger.info("removing entry from RecentScansDB")
        RecentScansDB.objects.filter(MD5=app_dic['md5']).delete()
        logger.info("RecentScanDB entry deleted")

        logger.info("Removing StaticAnalizerAndroid scan")
        StaticAnalyzerAndroid.objects.filter(MD5=app_dic["md5"]).delete()
        logger.info("StaticAnalizerAndroid scan %s removed" % app_dic["md5"])

        logger.info("removing %s from uploads" % app_dic["md5"])
        target = os.path.join(settings.UPLD_DIR, app_dic["md5"])

        try:
            if os.path.exists(target):
                logging.info("removing %s" % target)
                shutil.rmtree(target)
                logging.info("removed %s" % target)
            else:
                logging.info("upload directory %s does not exist" % target)
        except:
            return {"error" : "save_or_update failed"}, 500

        # After directories are deleted return this.
        return {"error" : "save_or_update failed"}, 500

    # Main fallback.
    return {"error" : "save_or_update failed"}, 500
