from pyrogram import Client
import asyncio
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'mindful-furnace-433013-p9-faafd585a99f.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name)").execute()
for result in results.get('files'):
    if(result.get('name') != "Request Storage"):
        f = open(result.get('name'), "w")
        f.close()
        file_id = result.get('id')
        request = service.files().get_media(fileId=file_id)
        filename = result.get('name')
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        service.files().delete(fileId=file_id).execute()
"""async def send_message(app):
        await app.send_message("yak8vlev", "сап")
apps = [Client("my_account2", 22791398, "ce792ff96c427cd0db6b4ae04d7916f7"),
        Client("my_account3", 20558172, "ff224348c90ed0201eed1003f0bd1881"),
        Client("my_account4", 23572907, "fe2ccbfb3b1f206394634f3a0c10d2bd"),
        Client("my_account5", 29647188, "4189745560d3c3a537d0a21961fedbf0"),
        Client("my_account6", 21058126, "4d12e2ff949907c6ed08d933e1bc9080"),
        Client("my_account7", 29140150, "0e1f41177fb442de612620affc7e8332"),
        Client("my_account8", 21565195, "5d1ed6cfd5b7d5c988a7809844980db1"),
        Client("my_account9", 23985186, "5c0b2ba6ce2b06370500fde068c1f6ce"),
        Client("my_account10", 22440260, "35dbed0c994ab28de25a76e50c01ebce"),
        Client("my_account12", 26906482, "a0b1f08b166bb9e63379b1717b7ea6ae"),
        Client("my_account13", 25333392, "60e5b3bb17f1c834cfb738f4eb136807"),
        Client("my_account14", 27097775, "f7ded6bf1d68d1b405623e53775e1165"),
        Client("my_account15", 22230216, "c108131c56a94c47021e2b3beb80a0aa"),
        Client("my_account16", 26339456, "5fa27d6f7094601d363cd9c6b22faa90"),
        Client("my_account17", 26579111, "1878a2d5e46fda2343abab9bca1ff9b0"),
        Client("my_account18", 24161989, "4ce483a0474b8449da582de0c980b7a7"),
        Client("my_account19", 20627208, "71e5b7c60de1939103438b1e53af395a"),
        Client("my_account20", 27409658, "fb97402f1a178d719b4b365612c1c442"),
        Client("my_account21", 28469403, "7eb2867c732ff6af29296e3a8c2ceaff"),
        Client("my_account22", 25426466 , "8a0cb8fa48ce4a5887e1d624d2e35c04"),
        Client("my_account23", 24344564, "a9a45c22aa282453f603d49d0b00fffe"),
        Client("my_account24", 13704325, "4330a0813c7555faa0c2aaadafb0a2f0"),
        Client("my_account25", 22182576, "a81779dc12cd2ec26a17e6bcc365e40b"),
        Client("my_account26", 29534866, "a01cf2ee71b4f1b858d2ca8791ba962f"),
        Client("my_account27", 26094829, "7b044a56dfb6a33090139c56fad9e299"),
        Client("my_account28", 29196093, "684718dabf5e2eae684b4457c901218b"),
        Client("my_account29", 29196093, "684718dabf5e2eae684b4457c901218b"),
        Client("my_account30", 29593455, "5084a8bddd2f90bab0dfc6ed2b3e1491"),
        Client("my_account31", 28442143, "85d7d7e00cc46649a9e48ab5b6c38654"),
        Client("my_account33", 29778203, "be50058c52e2c97253db5ac332a517da"),
        Client("my_account34", 16916828, "3519d189c2fd19470791696221b01bd0"),
        Client("my_account35", 22558070, "1caed5a17abf87cbbc43438250c7ca60"),
        Client("my_account36", 29260346, "cb499289e309de235e2d7eabf47eff41"),
        Client("my_account38", 14155282, "e77a1443815c8805cda805adaf21a4f6"),
        Client("my_account39", 20132141, "51f0a5421f6eba6345e5967a9184c6ea"),
        Client("my_account40", 24320939, "a34183b3be0c726ba5bddcf1b543a10b"),
        Client("my_account41", 26463021, "ea5cc2eeeb6266f997717fdd2f8c902a"),
        Client("my_account42", 21513497, "0aa1ea61b252cd2560dbde26ec9dfdfc"),
        Client("my_account43", 28904881, "b50244bafa64cb4f4ce068ab4c65933e"),
        Client("my_account44", 28704647, "017587b33cc3a8c3d321d0fe17053a02"),
        Client("my_account45", 21716679, "c7c2c6ff39190644927f46c6029c8da3"),
        Client("my_account46", 26788683, "8b5cb9b17d49d9c7d9ea588c5144bb77"),
        Client("my_account47", 20659634, "0ad93d9b5a39ca48bd908c041442994b"),
        Client("my_account48", 21647169, "397e34a32ca35464c24b66c3045e5cf4"),
        Client("my_account49", 27391719, "0c1e55406dbb54cce834ad7cc14f754d"),
        Client("my_account50", 27619393, "b7ea575334f66d2866115ea865ceac62"),
        Client("my_account51", 26595621, "84f17a28088c1f90169443cbe1a1e32c"),
        Client("my_account52", 27177111, "09ecded3dff265f69f7ba27a1398fc83"),
        Client("my_account53", 23459204, "ec882fa81c15c1003f53e3b18a32d96d"),
        Client("my_account54", 25640324, "ff4db948881d54501f9b7ca378963f62"),
        Client("my_account55", 23677041, "944c515035f381ee0afbeb8042308264"),
        Client("my_account56", 27209167, "f6abd807e3b69618ae753ac805a9d5c2"),
        Client("my_account57", 21073489, "96b49cb07d6d36af4137a8d55f3b16a0"),
        Client("my_account58", 23992875, "1aaa38c129fa2c7f068f046ae3484199"),
        Client("my_account59", 24819413, "e2f52f7817b59fc7669426f8aff16492"),
        Client("my_account60", 29408757, "2aa1698e14efc8011c6b61b3a3765ac2"),
        Client("my_account61", 20967535, "f017e9a520033fecf3eeeee00577e804"),
        Client("my_account62", 20076800, "d0e46246936511caed3ad86b4836b4a3"),
        Client("my_account63", 21543029, "db42c1a5c98edc1e73bfd7af3a2e62c3"),
        Client("my_account65", 23643220, "8c8ba3c72c06653e72df015c01d78443"),
        Client("my_account66", 24935738, "6c33fb190007ff9d6a8ff6d9f3735bcf"),
        Client("my_account67", 21372359, "41dc7e2e917193892816f2d1be8feebf"),
        Client("my_account68", 21717957, "2e23edded3de861977069b4f8406304b"),
        Client("my_account69", 21468290, "45d966c7bf06c6754770d6be94c203b5"),
        Client("my_account70", 22740393, "8c614380cc59178e6e51dba0c1ab4fd8"),
        Client("my_account71", 25722133, "ceff9e1665cc54301b579249939260ec"),
        Client("my_account73", 20673679, "e3648dafb424200c45eadcc36f9e86f3"),
        Client("my_account74", 24630984, "aea55250e20f47f80e176fe890207d63"),
        Client("my_account76", 12085401, "024b2e6555dc1275da7a09e6e06a726b"),
        Client("my_account77", 20110591, "15f09fa169d1a641b93b55bf353cddb1"),
        Client("my_account78", 20080608, "bbd2d2a4129732b7ff92270475a02644"),
        Client("my_account79", 24724540, "b9ab29dea83f557ee79a299d52fd45df"),
        Client("my_account80", 29120179, "adaec52c66c3c5366eaf382921d52e56"),
        Client("my_account81", 25824083, "515aec422080e3a3a6087d958fd88e94"),
        Client("my_account82", 21495841, "7059592a0319057b7253f3f12d66f722"),
        Client("my_account83", 25380302, "c8b5ba85e0b76d1c98cfff9d4aaf5046"),
        Client("my_account84", 23117421, "f0a686863f1282f15b5d67959f8a379d"),
        Client("my_account85", 24748590, "93765d99edf71cb077e6156f99f39871"),
        Client("my_account86", 26982776, "b44894b65df9e8abcacf7d0d83a22efc"),
        Client("my_account87", 28637545, "c5a8c2e9117c8af32526e5bf5402d128"),
        Client("my_account89", 29504086, "584637407d3cb4c4d7cf2a30cfd8c66e"),
        Client("my_account90", 20132635, "a02a33cf801550d4f9487603f2cadd1d"),
        Client("my_account91", 27372246, "627ea164ba0ee4f6bbe1854669e0fde8"),
        Client("my_account92", 27853307, "24b9225f094f35d685564ddc82f0c682"),
        Client("my_account93", 24590948, "f1b9f7814a7663620ed0efd8837bd40c"),
        Client("my_account95", 21327281, "1e04e08f4782838896ee10312ed95e2e"),
        Client("my_account96", 22671309, "438e5a16b4f5d7fa363776f4dcd47dae"),
        Client("my_account97", 21068732, "91007c765ddbc22f36ea0ff7a32148ae"),
        Client("my_account98", 20534031, "eae0c98012176535aa21a3935fbf98f7"),
        Client("my_account99", 20445166, "49d09a11b4f4fea72d157b7fe1c6528a"),
        Client("my_account100", 27635588, "63173c3993c2d9e7a4f6d7727524034f"),
        Client("my_account101", 28343693, "828452d8f2659806148429a8ac6248a9"),
        Client("my_account102", 28616915, "26568d64df52a17afb7eee222d436eca"),
        Client("my_account103", 9441991, "d7c918c93b5260664bd3f7df0524793a"),
        Client("my_account104", 25349294, "da3f7a96aa2b419e22d5c227d993f535"),
        Client("my_account105", 28210405, "3552caee4d373a04b9dde8d8fe9d978f"),
        Client("my_account106", 12052823, "fe790bf4bfe0ff5aa5396066d0ff4cc5"),
        Client("my_account107", 28417857, "c0a49575acb3e7553265c2e9ba6efc9f"),
        Client("my_account108", 21373787, "334ceb428e6c3ec60b5c8d3bf17e4b6e"),
        Client("my_account109", 21824586, "0362e28690d9c30cef85bafdd097ce98")]
async def main():
        async with app:
                await app.send_message("yak8vlev", "сап")

for app in apps:
        app.run(main())"""