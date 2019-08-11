#!/usr/bin/python3.6
import _pickle as pp
import sys

readfile = sys.argv[-1]

start = "          --------  --------"
end = "Input geometry:"

holdx = {}
holdx2 = {}
jag = []
mae = []
readx = False
#readfile = "FEB_IR02_ful.out"
with open(readfile) as rf:
    for lines in rf:
        if start in lines:
            readx = True
        elif end in lines and readx:
            readx = False
        elif len(lines.split()) == 2 and readx:
            #print(lines)
            j,m = lines.split()
            holdx[int(j)] = int(m)

#print(holdx)


# mae_data
#==========

maedata = ["atom_index",
"i_m_mmod_type",
"r_m_x_coord",
"r_m_y_coord",
"r_m_z_coord",
"i_m_residue_number",
"s_m_mmod_res",
"s_m_chain_name",
"i_m_color",
"r_m_charge1",
"r_m_charge2",
"s_m_pdb_residue_name",
"s_m_pdb_atom_name",
"i_m_atomic_number",
"i_m_formal_charge",
"i_m_visibility",
"s_m_color_rgb",
"s_m_atom_name",
"i_m_secondary_structure",
"s_m_label_format",
"i_m_label_color",
"s_m_label_user_text",
"r_ffio_x_vel",
"r_ffio_y_vel",
"r_ffio_z_vel",
"r_m_pdb_occupancy",
"r_m_pdb_tfactor",
"i_des_fullsystem_id",
"i_des_scratch_atom_num",
"i_des_scratch_entry_num",
"i_i_constraint",
"i_i_internal_atom_index",
"i_m_original_index",
"i_pa_atomindex",
"i_pdb_PDB_serial",
"i_pdb_seqres_index",
"s_pa_state",
"i_m_pdb_convert_problem",
"i_ppw_het",
"s_ppw_CCD_assignment_status",
"i_ppw_water",
"i_desmond_crystal_water"]


holdm = {}
try:
    holdm = pp.load(open("mae.dump", "rb"))
except:
    #print ("Error in loading mae file")
    with open("FEB_IR01_ful.mae") as mae:
        for lines in mae:
            if "<> <>" in lines:
                h = shlex.split(lines)
                holdm[int(h[0])] = {maedata[i]:h[i] for i in range(len(h))}
    pp.dump(holdm, open("mae.dump", "wb"))

#print ("[stage 3] time = {} secs".format(time.time() - t))


#---------------------------------------
def printdict(dd):
    atype = ["atom_index", "i_m_residue_number","s_m_pdb_residue_name", "s_m_pdb_atom_name"]
    s = []
    for key in atype:
        s.append("{} : {}".format(key, dd[key]))
    return "\n".join(s)

residue = []
for jag in holdx:
    if holdx[jag] != 0:
        print(jag, holdx[jag], holdm[holdx[jag]]["i_m_residue_number"])
        residue.append(holdm[holdx[jag]]["i_m_residue_number"])
r  =list(map(str, set(map(int,residue))))
print(",".join(r))
