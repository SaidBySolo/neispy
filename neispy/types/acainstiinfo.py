from typing_extensions import TypedDict

from neispy.types.base import BaseDict, NeisDict


class AcaInsTiInfoRowDict(BaseDict):
    ADMST_ZONE_NM: str
    "행정구역명"
    ACA_INSTI_SC_NM: str
    "학원교습소명"
    ACA_ASNUM: str
    "학원지정번호"
    ACA_NM: str
    "학원명"
    ESTBL_YMD: str
    "개설일자"
    REG_YMD: str
    "등록일자"
    REG_STTUS_NM: str
    "등록상태명"
    CAA_BEGIN_YMD: str
    "휴원시작일자"
    CAA_END_YMD: str
    "휴원종료일자"
    TOFOR_SMTOT: str
    "정원합계"
    DTM_RCPTN_ABLTY_NMPR_SMTOT: str
    "일시수용능력인원합계"
    REALM_SC_NM: str
    "분야명"
    LE_ORD_NM: str
    "교습계열명"
    LE_CRSE_LIST_NM: str
    "교습과정목록명"
    LE_CRSE_NM: str
    "교습과정명"
    PSNBY_THCC_CNTNT: str
    "인당수강료내용"
    THCC_OTHBC_YN: str
    "수강료공개여부"
    BRHS_ACA_YN: str
    "기숙사학원여부"
    FA_RDNZC: str
    "도로명우편번호"
    FA_RDNMA: str
    "도로명주소"
    FA_RDNDA: str
    "도로명상세주소"
    LOAD_DTM: str
    "수정일"


class AcaInsTiInfoDict(TypedDict):
    schoolInfo: NeisDict[AcaInsTiInfoRowDict]
