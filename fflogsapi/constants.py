'''
Various constant values that are typically useful for filtering queries.
'''


PARTY_SIZE_LIGHT_PARTY = 4
PARTY_SIZE_FULL_PARTY = 8

EVENT_TYPE_COMBATANT_INFO = 'combatantinfo'
EVENT_TYPE_BEGINCAST = 'begincast'
EVENT_TYPE_CAST = 'cast'
EVENT_TYPE_DAMAGE = 'damage'
EVENT_TYPE_CALCULATED_DAMAGE = 'calculateddamage'
EVENT_TYPE_HEAL = 'heal'
EVENT_TYPE_CALCULATED_HEAL = 'calculatedheal'
EVENT_TYPE_ABSORBED = 'absorbed'
EVENT_TYPE_APPLY_BUFF = 'applybuff'
EVENT_TYPE_APPLY_BUFF_STACK = 'applybuffstack'
EVENT_TYPE_REFRESH_BUFF = 'refreshbuff'
EVENT_TYPE_REMOVE_BUFF = 'removebuff'
EVENT_TYPE_REMOVE_BUFF_STACK = 'removebuffstack'
EVENT_TYPE_APPLY_DEBUFF = 'applydebuff'
EVENT_TYPE_REFRESH_DEBUFF = 'refreshdebuff'
EVENT_TYPE_REMOVE_DEBUFF = 'removedebuff'
EVENT_TYPE_LB_UPDATE = 'limitbreakupdate'
EVENT_ENCOUNTER_END = 'encounterend'

# FF Logs uses millisecond precision in its timestamps
TIMESTAMP_PRECISION = 1e-3
