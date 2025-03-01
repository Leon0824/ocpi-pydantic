from enum import Enum, IntEnum



class OcpiStatus(IntEnum):
    SUCCESS = 1000
    
    CLIENT_ERROR = 2000 
    INVALID_OR_MISSING_PARAMETERS = 2001 # for example: missing last_updated field in a PATCH request
    NOT_ENOUGH_INFORMATION = 2002 # for example: Authorization request with too little information
    UNKNOWN_LOCATION = 2003 # for example: Command: START_SESSION with unknown location
    UNKNOWN_TOKEN = 2004 # for example: 'real-time' authorization of an unknown Token

    SERVER_ERROR = 3000
    UNABLE_TO_USE_THE_CLIENTS_API = 3001
    UNSUPPORTED_VERSION = 3002
    NO_MATCHING_ENDPOINTS_OR_EXPECTED_ENDPOINTS_MISSING_BETWEEN_PARTIES = 3003

    HUB_ERROR = 4000
    UNKNOWN_RECEIVER = 4001 # TO address is unknown
    TIMEOUT_ON_FORWARDED_REQUEST = 4002 # message is forwarded, but request times out
    CONNECTION_PROBLEM = 4003 # receiving party is not connected



class OcpiPartyRoleEnum(str, Enum):
    '''
    OCPI 16.5.1 Role enum & OCPI 2.2

    - CPO: Charging Point Operator. Operates a network of Charge Points.
    - eMSP: e-Mobility Service Provider. Gives EV drivers access to charging services.
    - Hub: Can connect one or more CPOs to one or more eMSPs.
    - NAP: National Access Point. Provides a national database with all (public) charging locations. Information can be sent and retrieved from the NAP. This makes it different from a typical NSP.
    - NSP: Navigation Service Provider. Provides EV drivers with location information of Charge Points. Usually only interested in Location information.
    - Roaming Hub: See: Hub.
    - SCSP: Smart Charging Service Provider. Provides Smart Charging service to other parties. Might use a lot of different inputs to calculate Smart Charging Profiles.
    '''
    CPO = 'CPO'
    EMSP = 'EMSP'
    HUB = 'HUB'



class OcpiVersionNumberEnum(str, Enum):
    'List of known versions.'
    v221 = '2.2.1'



class OcpiModuleIdEnum(str, Enum):
    '''
    The Module identifiers for each endpoint are described in the beginning of each Module chapter.
    '''
    cdrs = 'cdrs'
    chargingprofiles = 'chargingprofiles'
    commands = 'commands'
    credentials = 'credentials' # Required for all implementations. The role field has no function for this module.
    hubclientinfo = 'hubclientinfo'
    locations = 'locations'
    sessions = 'sessions'
    tariffs = 'tariffs'
    tokens = 'tokens'
    versions = 'versions'



class OcpiInterfaceRoleEnum(str, Enum):
    '''
    - SENDER: Sender Interface implementation. Interface implemented by the owner of data, so the Receiver can Pull information from the data Sender/owner.
    - RECEIVER: Receiver Interface implementation. Interface implemented by the receiver of data, so the Sender/owner can Push information to the Receiver.
    '''
    SENDER = 'SENDER'
    RECEIVER = 'RECEIVER'



class OcpiCapabilityEnum(str, Enum):
    '''
    OCPI 8.4.3. Capability enum
    '''
    CHARGING_PROFILE_CAPABLE = 'CHARGING_PROFILE_CAPABLE' # The EVSE supports charging profiles.
    CHARGING_PREFERENCES_CAPABLE = 'CHARGING_PREFERENCES_CAPABLE' # The EVSE supports charging profiles.
    CHIP_CARD_SUPPORT = 'CHIP_CARD_SUPPORT' # EVSE has a payment terminal that supports chip cards.
    CONTACTLESS_CARD_SUPPORT = 'CONTACTLESS_CARD_SUPPORT' # EVSE has a payment terminal that supports contactless cards.
    CREDIT_CARD_PAYABLE = 'CREDIT_CARD_PAYABLE' # EVSE has a payment terminal that makes it possible to pay for charging using a credit card.
    DEBIT_CARD_PAYABLE = 'DEBIT_CARD_PAYABLE' # EVSE has a payment terminal that makes it possible to pay for charging using a debit card.
    PED_TERMINAL = 'PED_TERMINAL' # EVSE has a payment terminal with a pin-code entry device.
    REMOTE_START_STOP_CAPABLE = 'REMOTE_START_STOP_CAPABLE' # The EVSE can remotely be started/stopped.
    RESERVABLE = 'RESERVABLE' # The EVSE can be reserved.
    RFID_READER = 'RFID_READER' # Charging at this EVSE can be authorized with an RFID token.
    START_SESSION_CONNECTOR_REQUIRED = 'START_SESSION_CONNECTOR_REQUIRED' # When a StartSession is sent to this EVSE, the MSP is required to add the optional connector_id field in the StartSession object.
    TOKEN_GROUP_CAPABLE = 'TOKEN_GROUP_CAPABLE' # This EVSE supports token groups, two or more tokens work as one, so that a session can be started with one token and stopped with another (handy when a card and key-fob are given to the EV-driver).
    UNLOCK_CAPABLE = 'UNLOCK_CAPABLE' # Connectors have mechanical lock that can be requested by the eMSP to be unlocked.



class OcpiConnectorFormatEnum(str, Enum):
    '''
    OCPI 8.4.4. ConnectorFormat enum
    '''
    SOCKET = 'SOCKET' # The connector is a socket; the EV user needs to bring a fitting plug.
    CABLE = 'CABLE' # The connector is an attached cable; the EV users car needs to have a fitting inlet.



class OcpiConnectorTypeEnum(str, Enum):
    '''
    OCPI 8.4.5. ConnectorType enum
    '''
    CHADEMO = 'CHADEMO' # The connector type is CHAdeMO, DC
    CHAOJI = 'CHAOJI' # The ChaoJi connector.
    DOMESTIC_A = 'DOMESTIC_A' # Standard/Domestic household, type "A", NEMA 1-15, 2 pins
    DOMESTIC_B = 'DOMESTIC_B' # Standard/Domestic household, type "B", NEMA 5-15, 3 pins
    DOMESTIC_C = 'DOMESTIC_C' # Standard/Domestic household, type "C", CEE 7/17, 2 pins
    DOMESTIC_D = 'DOMESTIC_D' # Standard/Domestic household, type "D", 3 pin
    DOMESTIC_E = 'DOMESTIC_E' # Standard/Domestic household, type "E", CEE 7/5 3 pins
    DOMESTIC_F = 'DOMESTIC_F' # Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins
    DOMESTIC_G = 'DOMESTIC_G' # Standard/Domestic household, type "G", BS 1363, Commonwealth, 3 pins
    DOMESTIC_H = 'DOMESTIC_H' # Standard/Domestic household, type "H", SI-32, 3 pins
    DOMESTIC_I = 'DOMESTIC_I' # Standard/Domestic household, type "I", AS 3112, 3 pins
    DOMESTIC_J = 'DOMESTIC_J' # Standard/Domestic household, type "J", SEV 1011, 3 pins
    DOMESTIC_K = 'DOMESTIC_K' # Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins
    DOMESTIC_L = 'DOMESTIC_L' # Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins
    DOMESTIC_M = 'DOMESTIC_M' # Standard/Domestic household, type "M", BS 546, 3 pins
    DOMESTIC_N = 'DOMESTIC_N' # Standard/Domestic household, type "N", NBR 14136, 3 pins
    DOMESTIC_O = 'DOMESTIC_O' # Standard/Domestic household, type "O", TIS 166-2549, 3 pins
    GBT_AC = 'GBT_AC' # Guobiao GB/T 20234.2 AC socket/connector
    GBT_DC = 'GBT_DC' # Guobiao GB/T 20234.3 DC connector
    IEC_60309_2_single_16 = 'IEC_60309_2_single_16' # IEC 60309-2 Industrial Connector single phase 16 amperes (usually blue)
    IEC_60309_2_three_16 = 'IEC_60309_2_three_16' # IEC 60309-2 Industrial Connector three phases 16 amperes (usually red)
    IEC_60309_2_three_32 = 'IEC_60309_2_three_32' # IEC 60309-2 Industrial Connector three phases 32 amperes (usually red)
    IEC_60309_2_three_64 = 'IEC_60309_2_three_64' # IEC 60309-2 Industrial Connector three phases 64 amperes (usually red)
    IEC_62196_T1 = 'IEC_62196_T1' # IEC 62196 Type 1 "SAE J1772"
    IEC_62196_T1_COMBO = 'IEC_62196_T1_COMBO' # Combo Type 1 based, DC
    IEC_62196_T2 = 'IEC_62196_T2' # IEC 62196 Type 2 "Mennekes"
    IEC_62196_T2_COMBO = 'IEC_62196_T2_COMBO' # Combo Type 2 based, DC
    IEC_62196_T3A = 'IEC_62196_T3A' # IEC 62196 Type 3A
    IEC_62196_T3C = 'IEC_62196_T3C' # IEC 62196 Type 3C "Scame"
    NEMA_5_20 = 'NEMA_5_20' # NEMA 5-20, 3 pins
    NEMA_6_30 = 'NEMA_6_30' # NEMA 6-30, 3 pins
    NEMA_6_50 = 'NEMA_6_50' # NEMA 6-50, 3 pins
    NEMA_10_30 = 'NEMA_10_30' # NEMA 10-30, 3 pins
    NEMA_10_50 = 'NEMA_10_50' # NEMA 10-50, 3 pins
    NEMA_14_30 = 'NEMA_14_30' # NEMA 14-30, 3 pins, rating of 30 A
    NEMA_14_50 = 'NEMA_14_50' # NEMA 14-50, 3 pins, rating of 50 A
    PANTOGRAPH_BOTTOM_UP = 'PANTOGRAPH_BOTTOM_UP' # On-board Bottom-up-Pantograph typically for bus charging
    PANTOGRAPH_TOP_DOWN = 'PANTOGRAPH_TOP_DOWN' # Off-board Top-down-Pantograph typically for bus charging
    TESLA_R = 'TESLA_R' # Tesla Connector "Roadster"-type (round, 4 pin)
    TESLA_S = 'TESLA_S' # Tesla Connector "Model-S"-type (oval, 5 pin)



class OcpiEnergySourceCategoryEnum(str, Enum):
    '''
    OCPI 8.4.8. EnergySourceCategory enum
    '''
    NUCLEAR = 'NUCLEAR'
    GENERAL_FOSSIL = 'GENERAL_FOSSIL'
    COAL = 'COAL'
    GAS = 'GAS'
    GENERAL_GREEN = 'GENERAL_GREEN'
    SOLAR = 'SOLAR'
    WIND = 'WIND'
    WATER = 'WATER'



class OcpiEnvironmentalImpactCategoryEnum(str, Enum):
    '''
    OCPI 8.4.10. EnvironmentalImpactCategory enum
    '''
    NUCLEAR_WASTE = 'NUCLEAR_WASTE' # Produced nuclear waste in grams per kilowatthour.
    CARBON_DIOXIDE = 'CARBON_DIOXIDE' # Exhausted carbon dioxide in grams per kilowatthour.



class OcpiFacilityEnum(str, Enum):
    '''
    OCPI 8.4.12. Facility enum
    '''
    HOTEL = 'HOTEL'
    RESTAURANT = 'RESTAURANT'
    CAFE = 'CAFE'
    MALL = 'MALL'
    SUPERMARKET = 'SUPERMARKET'
    SPORT = 'SPORT'
    RECREATION_AREA = 'RECREATION_AREA'
    NATURE = 'NATURE'
    MUSEUM = 'MUSEUM'
    BIKE_SHARING = 'BIKE_SHARING'
    BUS_STOP = 'BUS_STOP'
    TAXI_STAND = 'TAXI_STAND'
    TRAM_STOP = 'TRAM_STOP'
    METRO_STATION = 'METRO_STATION'
    TRAIN_STATION = 'TRAIN_STATION'
    AIRPORT = 'AIRPORT'
    PARKING_LOT = 'PARKING_LOT'
    CARPOOL_PARKING = 'CARPOOL_PARKING'
    FUEL_STATION = 'FUEL_STATION'
    WIFI = 'WIFI'



class OcpiImageCategoryEnum(str, Enum):
    CHARGER = 'CHARGER'
    ENTRANCE = 'ENTRANCE'
    LOCATION = 'LOCATION'
    NETWORK = 'NETWORK'
    OPERATOR = 'OPERATOR'
    OTHER = 'OTHER'
    OWNER = 'OWNER'



class OcpiParkingRestrictionEnum(str, Enum):
    '''
    OCPI 8.4.17. ParkingRestriction enum
    '''
    EV_ONLY = 'EV_ONLY' # Reserved parking spot for electric vehicles.
    PLUGGED = 'PLUGGED' # Parking is only allowed while plugged in (charging).
    DISABLED = 'DISABLED' # Reserved parking spot for disabled people with valid ID.
    CUSTOMERS = 'CUSTOMERS' # Parking spot for customers/guests only, for example in case of a hotel or shop.
    MOTORCYCLES = 'MOTORCYCLES' # Parking spot only suitable for (electric) motorcycles or scooters.



class OcpiParkingTypeEnum(str, Enum):
    '''
    OCPI 8.4.18. ParkingType enum
    '''
    ALONG_MOTORWAY  = 'ALONG_MOTORWAY' # Location on a parking facility/rest area along a motorway, freeway, interstate, highway etc.
    PARKING_GARAGE = 'PARKING_GARAGE' # Multistorey car park.
    PARKING_LOT = 'PARKING_LOT' # A cleared area that is intended for parking vehicles, i.e. at super markets, bars, etc.
    ON_DRIVEWAY = 'ON_DRIVEWAY' # Location is on the driveway of a house/building.
    ON_STREET = 'ON_STREET' # Parking in public space along a street.
    UNDERGROUND_GARAGE = 'UNDERGROUND_GARAGE' # Multistorey car park, mainly underground.



class OcpiPowerTypeEnum(str, Enum):
    '''
    OCPI 8.4.19. PowerType enum
    '''
    AC_1_PHASE = 'AC_1_PHASE' # AC single phase.
    AC_2_PHASE = 'AC_2_PHASE' # AC two phases, only two of the three available phases connected.
    AC_2_PHASE_SPLIT = 'AC_2_PHASE_SPLIT' # AC two phases using split phase system.
    AC_3_PHASE = 'AC_3_PHASE' # AC three phases.
    DC = 'DC' # Direct Current.



class OcpiStatusEnum(str, Enum):
    '''
    OCPI 8.4.22. Status enum
    '''
    AVAILABLE = 'AVAILABLE' # The EVSE/Connector is able to start a new charging session.
    BLOCKED = 'BLOCKED' # The EVSE/Connector is not accessible because of a physical barrier, i.e. a car.
    CHARGING = 'CHARGING' # The EVSE/Connector is in use.
    INOPERATIVE = 'INOPERATIVE' # The EVSE/Connector is not yet active, or temporarily not available for use, but not broken or defect.
    OUTOFORDER = 'OUTOFORDER' # The EVSE/Connector is currently out of order, some part/components may be broken/defect.
    PLANNED = 'PLANNED' # The EVSE/Connector is planned, will be operating soon.
    REMOVED = 'REMOVED' # The EVSE/Connector was discontinued/removed.
    RESERVED = 'RESERVED' # The EVSE/Connector is reserved for a particular EV driver and is unavailable for other drivers.
    UNKNOWN = 'UNKNOWN' # No status information available (also used when offline).



class OcpiTokenTypeEnum(str, Enum):
    '''
    OCPI 12.4.4. TokenType enum
    '''
    AD_HOC_USER = 'AD_HOC_USER' # One time use Token ID generated by a server (or App.)
    APP_USER = 'APP_USER' # Token ID generated by a server (or App.) to identify a user of an App.
    OTHER = 'OTHER' # Other type of token
    RFID = 'RFID' # RFID