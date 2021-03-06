# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/download_install_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/download_install_state.proto',
  package='mg.protocol.download_install_state',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#protos/download_install_state.proto\x12\"mg.protocol.download_install_state\".\n\x07License\x12\x12\n\nidentifier\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\r\"T\n\tInstaller\x12\x12\n\nidentifier\x18\x01 \x02(\t\x12\x18\n\x10manifest_version\x18\x02 \x01(\r\x12\x19\n\x11installed_version\x18\x03 \x01(\r\"Z\n\rRegistryEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\x12\x14\n\x0cnumber_value\x18\x04 \x01(\r\"\x8a\x01\n\x05\x43hunk\x12\x10\n\x08\x63hunk_id\x18\x01 \x02(\r\x12\x13\n\x0bis_required\x18\x02 \x02(\x08\x12\x15\n\ris_downloaded\x18\x03 \x02(\x08\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x10\n\x08uplay_id\x18\x05 \x01(\r\x12\x0c\n\x04tags\x18\x06 \x01(\t\x12\x11\n\tuplay_ids\x18\x07 \x03(\r\"\x18\n\x08Shortcut\x12\x0c\n\x04name\x18\x01 \x02(\t\"1\n\rTextFileEntry\x12\x10\n\x08\x66ileName\x18\x01 \x02(\t\x12\x0e\n\x06locale\x18\x02 \x02(\t\"b\n\x0cTextFileList\x12\x10\n\x08rootPath\x18\x01 \x01(\t\x12@\n\x05\x66iles\x18\x02 \x03(\x0b\x32\x31.mg.protocol.download_install_state.TextFileEntry\"\xc8\x07\n\x14\x44ownloadInstallState\x12\x15\n\rmanifest_sha1\x18\x01 \x01(\t\x12\x18\n\x10\x64ownloading_sha1\x18\n \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x19\n\x11selected_language\x18\x03 \x01(\t\x12=\n\x08licenses\x18\x04 \x03(\x0b\x32+.mg.protocol.download_install_state.License\x12\x41\n\ninstallers\x18\x05 \x03(\x0b\x32-.mg.protocol.download_install_state.Installer\x12\x39\n\x06\x63hunks\x18\x06 \x03(\x0b\x32).mg.protocol.download_install_state.Chunk\x12\x15\n\rshortcut_name\x18\x0b \x01(\t\x12?\n\tshortcuts\x18\r \x03(\x0b\x32,.mg.protocol.download_install_state.Shortcut\x12K\n\x10registry_entries\x18\x0f \x03(\x0b\x32\x31.mg.protocol.download_install_state.RegistryEntry\x12\x11\n\tlanguages\x18\x11 \x03(\t\x12\x1d\n\x15\x64ownloading_languages\x18\x12 \x03(\t\x12\x16\n\x0epatch_required\x18\x13 \x01(\x08\x12\'\n\x1f\x62ytes_downloaded_on_patch_start\x18\x14 \x01(\x04\x12\x30\n(required_bytes_downloaded_on_patch_start\x18\x15 \x01(\x04\x12\x11\n\tgame_name\x18\x16 \x01(\t\x12\x45\n\x0breadmeFiles\x18\x17 \x01(\x0b\x32\x30.mg.protocol.download_install_state.TextFileList\x12\x45\n\x0bmanualFiles\x18\x18 \x01(\x0b\x32\x30.mg.protocol.download_install_state.TextFileList\x12\x14\n\x0cgame_version\x18\x19 \x01(\t\x12\x1b\n\x13installed_languages\x18\x1a \x03(\t\x12\x18\n\x10installed_addons\x18\x1b \x03(\r\x12\x10\n\x08uplay_id\x18\x1c \x01(\r\x12&\n\x1einvalidate_game_token_required\x18\x1d \x01(\x08\x12$\n\x15\x65pic_run_installation\x18\x1e \x01(\x08:\x05\x66\x61lse')
)




_LICENSE = _descriptor.Descriptor(
  name='License',
  full_name='mg.protocol.download_install_state.License',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='mg.protocol.download_install_state.License.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mg.protocol.download_install_state.License.version', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=121,
)


_INSTALLER = _descriptor.Descriptor(
  name='Installer',
  full_name='mg.protocol.download_install_state.Installer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='mg.protocol.download_install_state.Installer.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest_version', full_name='mg.protocol.download_install_state.Installer.manifest_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installed_version', full_name='mg.protocol.download_install_state.Installer.installed_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=207,
)


_REGISTRYENTRY = _descriptor.Descriptor(
  name='RegistryEntry',
  full_name='mg.protocol.download_install_state.RegistryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mg.protocol.download_install_state.RegistryEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='mg.protocol.download_install_state.RegistryEntry.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='mg.protocol.download_install_state.RegistryEntry.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_value', full_name='mg.protocol.download_install_state.RegistryEntry.number_value', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=299,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='mg.protocol.download_install_state.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_id', full_name='mg.protocol.download_install_state.Chunk.chunk_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_required', full_name='mg.protocol.download_install_state.Chunk.is_required', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_downloaded', full_name='mg.protocol.download_install_state.Chunk.is_downloaded', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='mg.protocol.download_install_state.Chunk.language', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplay_id', full_name='mg.protocol.download_install_state.Chunk.uplay_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='mg.protocol.download_install_state.Chunk.tags', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplay_ids', full_name='mg.protocol.download_install_state.Chunk.uplay_ids', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=440,
)


_SHORTCUT = _descriptor.Descriptor(
  name='Shortcut',
  full_name='mg.protocol.download_install_state.Shortcut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mg.protocol.download_install_state.Shortcut.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=466,
)


_TEXTFILEENTRY = _descriptor.Descriptor(
  name='TextFileEntry',
  full_name='mg.protocol.download_install_state.TextFileEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='mg.protocol.download_install_state.TextFileEntry.fileName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='mg.protocol.download_install_state.TextFileEntry.locale', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=517,
)


_TEXTFILELIST = _descriptor.Descriptor(
  name='TextFileList',
  full_name='mg.protocol.download_install_state.TextFileList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rootPath', full_name='mg.protocol.download_install_state.TextFileList.rootPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='mg.protocol.download_install_state.TextFileList.files', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=617,
)


_DOWNLOADINSTALLSTATE = _descriptor.Descriptor(
  name='DownloadInstallState',
  full_name='mg.protocol.download_install_state.DownloadInstallState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='manifest_sha1', full_name='mg.protocol.download_install_state.DownloadInstallState.manifest_sha1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloading_sha1', full_name='mg.protocol.download_install_state.DownloadInstallState.downloading_sha1', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mg.protocol.download_install_state.DownloadInstallState.version', index=2,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selected_language', full_name='mg.protocol.download_install_state.DownloadInstallState.selected_language', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='licenses', full_name='mg.protocol.download_install_state.DownloadInstallState.licenses', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installers', full_name='mg.protocol.download_install_state.DownloadInstallState.installers', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='mg.protocol.download_install_state.DownloadInstallState.chunks', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortcut_name', full_name='mg.protocol.download_install_state.DownloadInstallState.shortcut_name', index=7,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortcuts', full_name='mg.protocol.download_install_state.DownloadInstallState.shortcuts', index=8,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_entries', full_name='mg.protocol.download_install_state.DownloadInstallState.registry_entries', index=9,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languages', full_name='mg.protocol.download_install_state.DownloadInstallState.languages', index=10,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloading_languages', full_name='mg.protocol.download_install_state.DownloadInstallState.downloading_languages', index=11,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch_required', full_name='mg.protocol.download_install_state.DownloadInstallState.patch_required', index=12,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_downloaded_on_patch_start', full_name='mg.protocol.download_install_state.DownloadInstallState.bytes_downloaded_on_patch_start', index=13,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_bytes_downloaded_on_patch_start', full_name='mg.protocol.download_install_state.DownloadInstallState.required_bytes_downloaded_on_patch_start', index=14,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_name', full_name='mg.protocol.download_install_state.DownloadInstallState.game_name', index=15,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readmeFiles', full_name='mg.protocol.download_install_state.DownloadInstallState.readmeFiles', index=16,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manualFiles', full_name='mg.protocol.download_install_state.DownloadInstallState.manualFiles', index=17,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_version', full_name='mg.protocol.download_install_state.DownloadInstallState.game_version', index=18,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installed_languages', full_name='mg.protocol.download_install_state.DownloadInstallState.installed_languages', index=19,
      number=26, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installed_addons', full_name='mg.protocol.download_install_state.DownloadInstallState.installed_addons', index=20,
      number=27, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplay_id', full_name='mg.protocol.download_install_state.DownloadInstallState.uplay_id', index=21,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invalidate_game_token_required', full_name='mg.protocol.download_install_state.DownloadInstallState.invalidate_game_token_required', index=22,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epic_run_installation', full_name='mg.protocol.download_install_state.DownloadInstallState.epic_run_installation', index=23,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=1588,
)

_TEXTFILELIST.fields_by_name['files'].message_type = _TEXTFILEENTRY
_DOWNLOADINSTALLSTATE.fields_by_name['licenses'].message_type = _LICENSE
_DOWNLOADINSTALLSTATE.fields_by_name['installers'].message_type = _INSTALLER
_DOWNLOADINSTALLSTATE.fields_by_name['chunks'].message_type = _CHUNK
_DOWNLOADINSTALLSTATE.fields_by_name['shortcuts'].message_type = _SHORTCUT
_DOWNLOADINSTALLSTATE.fields_by_name['registry_entries'].message_type = _REGISTRYENTRY
_DOWNLOADINSTALLSTATE.fields_by_name['readmeFiles'].message_type = _TEXTFILELIST
_DOWNLOADINSTALLSTATE.fields_by_name['manualFiles'].message_type = _TEXTFILELIST
DESCRIPTOR.message_types_by_name['License'] = _LICENSE
DESCRIPTOR.message_types_by_name['Installer'] = _INSTALLER
DESCRIPTOR.message_types_by_name['RegistryEntry'] = _REGISTRYENTRY
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['Shortcut'] = _SHORTCUT
DESCRIPTOR.message_types_by_name['TextFileEntry'] = _TEXTFILEENTRY
DESCRIPTOR.message_types_by_name['TextFileList'] = _TEXTFILELIST
DESCRIPTOR.message_types_by_name['DownloadInstallState'] = _DOWNLOADINSTALLSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

License = _reflection.GeneratedProtocolMessageType('License', (_message.Message,), dict(
  DESCRIPTOR = _LICENSE,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.License)
  ))
_sym_db.RegisterMessage(License)

Installer = _reflection.GeneratedProtocolMessageType('Installer', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLER,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.Installer)
  ))
_sym_db.RegisterMessage(Installer)

RegistryEntry = _reflection.GeneratedProtocolMessageType('RegistryEntry', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRYENTRY,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.RegistryEntry)
  ))
_sym_db.RegisterMessage(RegistryEntry)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), dict(
  DESCRIPTOR = _CHUNK,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.Chunk)
  ))
_sym_db.RegisterMessage(Chunk)

Shortcut = _reflection.GeneratedProtocolMessageType('Shortcut', (_message.Message,), dict(
  DESCRIPTOR = _SHORTCUT,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.Shortcut)
  ))
_sym_db.RegisterMessage(Shortcut)

TextFileEntry = _reflection.GeneratedProtocolMessageType('TextFileEntry', (_message.Message,), dict(
  DESCRIPTOR = _TEXTFILEENTRY,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.TextFileEntry)
  ))
_sym_db.RegisterMessage(TextFileEntry)

TextFileList = _reflection.GeneratedProtocolMessageType('TextFileList', (_message.Message,), dict(
  DESCRIPTOR = _TEXTFILELIST,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.TextFileList)
  ))
_sym_db.RegisterMessage(TextFileList)

DownloadInstallState = _reflection.GeneratedProtocolMessageType('DownloadInstallState', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADINSTALLSTATE,
  __module__ = 'protos.download_install_state_pb2'
  # @@protoc_insertion_point(class_scope:mg.protocol.download_install_state.DownloadInstallState)
  ))
_sym_db.RegisterMessage(DownloadInstallState)


# @@protoc_insertion_point(module_scope)
