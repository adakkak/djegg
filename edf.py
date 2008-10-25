from __future__ import with_statement
from struct import unpack

class EDF:
    def __init__(self, file_name):
        self.file_name = file_name
        self.header = {}
        self.samples = []

        self.read_edf()

    def to_int(self, *args):
        return map(lambda x: int(x), *args)

    def twos_complement(self, s):
        # sample records are stored in little endian format 
        # as a short in 2s complement
        return ~unpack('<h', s)[0] + 1

    def read_edf(self):
        with(open(self.file_name, "rb")) as file:
            # read header
            self.header["version"] = file.read(8).strip()
            self.header["patient_id"] = file.read(80).strip()
            self.header["record_id"] = file.read(80).strip()
            self.header["startdate"] = file.read(8).strip()
            self.header["starttime"] = file.read(8).strip()
            self.header["header_length"] = int(file.read(8))

            reserved = file.read(44)

            self.header["num_of_records"] = int(file.read(8))
            self.header["record_duration"] = int(file.read(8))
            ns = self.header["num_of_signals"] = int(file.read(4))

            self.header["labels"] = [file.read(16).strip() for i in xrange(ns)]
            self.header["transducer_types"] = [file.read(80).strip() for i in xrange(ns)]
            self.header["physical_dims"] = [file.read(8).strip() for i in xrange(ns)]
            self.header["physical_mins"] = self.to_int([file.read(8) for i in xrange(ns)])
            self.header["physical_maxs"] = self.to_int([file.read(8) for i in xrange(ns)])
            self.header["dig_mins"] = self.to_int([file.read(8) for i in xrange(ns)])
            self.header["dig_maxs"] = self.to_int([file.read(8) for i in xrange(ns)])
            self.header["prefilterings"] = [file.read(80).strip() for i in xrange(ns)]
            self.header["nrs"] = self.to_int([file.read(8) for i in xrange(ns)])
            reserved = [file.read(32) for i in xrange(ns)]

            # read samples
            self.samples = [[] for i in xrange(ns)]
            for i in xrange(ns):
                for j in xrange(self.header["nrs"][i]):
                    self.samples[i].append(self.twos_complement(file.read(2)))

#file_name = "test_data/st7132j0.rec"
#edf =  EDF(file_name)
#print edf.samples[0]
