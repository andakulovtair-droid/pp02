-- Процедура 1: Добавить или обновить один контакт (Upsert)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    -- Проверка: только цифры и длина >= 10
    IF p_phone ~ '^[0-9]+$' AND length(p_phone) >= 10 THEN
        INSERT INTO contacts (name, phone) VALUES (p_name, p_phone)
        ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;
    ELSE
        RAISE NOTICE 'Ошибка: Номер % содержит буквы или слишком короткий!', p_phone;
    END IF;
END; $$;

-- Процедура 2: Массовая вставка (Bulk Insert)
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE i INTEGER;
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        -- Проверка: только цифры и длина >= 10
        IF p_phones[i] ~ '^[0-9]+$' AND length(p_phones[i]) >= 10 THEN
            INSERT INTO contacts(name, phone) VALUES (p_names[i], p_phones[i])
            ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;
        ELSE
            RAISE NOTICE 'Контакт % пропущен: номер % невалиден', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END; $$;

-- Процедура 3: Удаление (Delete)
CREATE OR REPLACE PROCEDURE delete_contact(p_identity TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p_identity OR phone = p_identity;
END; $$;