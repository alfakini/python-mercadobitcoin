import os
import inspect
import vcr

def build_path(function):
    return os.path.join(os.path.dirname(inspect.getfile(function)),
                        'cassettes',
                        function.__module__.split('.')[1],
                        function.__name__ + '.yml')

vcr = vcr.config.VCR(
  func_path_generator=build_path,
  cassette_library_dir='tests/cassettes',
  match_on=['uri', 'method'],
  decode_compressed_response=True,
  record_mode='once'
)
