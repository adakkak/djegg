from __future__ import with_statement
from struct import unpack

class EDF:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "rb")

        self.header = {}
        self.samples = []

        self.read_header()

        self.samples = [[] for i in xrange(self.ns)]

        self.read_samples()
        self.n = 0

    def next_sample(self):
#        return self.read_samples().next()
        next_sample = map(lambda x: 0 if self.n > len(x) else x[self.n], self.samples)
        self.n += 1
        return next_sample 

    def to_int(self, *args):
        return map(lambda x: int(x), *args)

    def twos_complement(self, s):
        # sample records are stored in little endian format 
        # as a short in 2s complement
        return ~unpack('<h', s)[0] + 1

    def read_header(self):
        self.header["version"] = self.file.read(8).strip()
        self.header["patient_id"] = self.file.read(80).strip()
        self.header["record_id"] = self.file.read(80).strip()
        self.header["startdate"] = self.file.read(8).strip()
        self.header["starttime"] = self.file.read(8).strip()
        self.header["header_length"] = int(self.file.read(8))

        reserved = self.file.read(44)

        self.header["num_of_records"] = int(self.file.read(8))
        self.header["record_duration"] = int(self.file.read(8))
        self.ns = self.header["num_of_signals"] = int(self.file.read(4))

        self.header["labels"] = [self.file.read(16).strip() for i in xrange(self.ns)]
        self.header["transducer_types"] = [self.file.read(80).strip() for i in xrange(self.ns)]
        self.header["physical_dims"] = [self.file.read(8).strip() for i in xrange(self.ns)]
        self.header["physical_mins"] = self.to_int([self.file.read(8) for i in xrange(self.ns)])
        self.header["physical_maxs"] = self.to_int([self.file.read(8) for i in xrange(self.ns)])
        self.header["dig_mins"] = self.to_int([self.file.read(8) for i in xrange(self.ns)])
        self.header["dig_maxs"] = self.to_int([self.file.read(8) for i in xrange(self.ns)])
        self.header["prefilterings"] = [self.file.read(80).strip() for i in xrange(self.ns)]
        self.header["nrs"] = self.to_int([self.file.read(8) for i in xrange(self.ns)])
        reserved = [self.file.read(32) for i in xrange(self.ns)]

    def read_samples(self):
        for i in xrange(self.ns): 
#            samples = []
            for j in xrange(self.header["nrs"][i]): 
                sample = self.twos_complement(self.file.read(2))
                self.samples[i].append(sample)
#                samples.append(sample)
#            yield samples

#file_name = "test_data/st7132j0.rec"
#edf =  EDF(file_name)
#print edf.next_sample()
#print edf.next_sample()
#print edf.next_sample()
#print edf.next_sample()
