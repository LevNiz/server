CREATED = 'created'
ON_WAY = 'on_way'
ARRIVED = 'arrived'
DONE = 'done'

PACKAGE_STATUS = ((CREATED, 'Оформлен'), (ON_WAY, 'В пути'), (ARRIVED, 'Прибыл'), (DONE, 'Выполнен'))

PAID = 'paid'
UNPAID = 'unpaid'
PAYMENT_STATUS = ((PAID, 'Оплачено'), (UNPAID, 'Не оплачено'))

ALAKETEM = 'alaketem'
BEREM = 'berem'
ALAKETEM_TYPE = ((ALAKETEM, 'Возьму собой'), (BEREM, 'Отдам'))

IN = 'in'
OUT = 'out'
BOTH = 'both'
DEPOT_TYPE = ((IN, 'in'), (OUT, 'out'), (BOTH, 'both'))

DEPOT = 'depot'
CUSTOM = 'custom'
ADDRESS_TYPE = ((DEPOT, 'Склад'), (CUSTOM, 'Custom'))

CONFIRMED = 'confirmed'
IN_PROGRESS = 'in_progress'
BOUGHT = 'bought'
SENT = 'sent'
BUYER_REQUEST_STATUS = ((CREATED, 'Создано'), (CONFIRMED, 'Подтверждено'), (IN_PROGRESS, 'В процессе'),
                        (BOUGHT, 'Куплено'), (SENT, "Отправлено"))


NEW = 'new'
PACKING = 'packing'
DELIVERING = 'delivering'
DELIVERED = 'delivered'
REJECTED = 'rejected'
CLIENT_REJECT = 'client_reject'
ORDER_STATUS = ((NEW, 'Новый'), (PACKING, 'Упаковывается'), (DELIVERING, 'В пути'), (DELIVERED, 'Доставлено'),
                (REJECTED, 'Отказано'), (CLIENT_REJECT, 'Отменен'))

MALE = 'male'
FEMALE = 'female'
KIDS = 'kids'
GENDER = ((MALE, 'Мужской'), (FEMALE, 'Женский'), (KIDS, 'Детский'))
