from typing import Any, NamedTuple, Tuple

class hostinfo(NamedTuple):
    hostname: Any
    cores: Any

def get_job_machines(custom_input: Any | None = ...) -> Tuple[hostinfo]: ...
def parse_custom_input(custom_input: str) -> Tuple[hostinfo]: ...
def parse_hosts_sge(host_file_name: str) -> Tuple[hostinfo]: ...
def parse_hosts_lsf(host_list_str: str) -> Tuple[hostinfo]: ...
def parse_hosts_ccs(host_list_str: str) -> Tuple[hostinfo]: ...
def parse_hosts_pbs(pbs_node_file: str) -> Tuple[hostinfo]: ...
def parse_hosts_slurm(host_list_str: str) -> Tuple[hostinfo]: ...
