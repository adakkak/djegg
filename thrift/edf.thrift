struct Header {
    1:string    version,
    2:string    patient_id,
    3:string    record_id,
    4:string    startdate,
    5:string    starttime,
    6:i32       header_length,

    7:i32       num_of_records,
    8:i32       record_duration,
    9:i32       num_of_signals,

    10:list<string>     labels,
    11:list<string>     transducer_types,
    12:list<string>     physical_dims,
    13:list<i32>        physical_mins,
    14:list<i32>        physical_maxs,
    15:list<i32>        dig_mins,
    16:list<i32>        dig_maxs,
    17:list<string>     prefilterings,
    18:list<i32>        nrs
}

typedef list<i32> Sample

service Request {
    async void set_file(1:string file_name),
    Header get_header(),
    Sample get_sample(),
    async void set_header(1:Header header)
}
