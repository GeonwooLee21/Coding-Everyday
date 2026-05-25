"""
===============================================================
Day 5: Python Class Practice — Gym Membership System
Day 5: Python 클래스 연습 — 헬스장 회원권 시스템
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260525
===============================================================

학습 목표 / Learning Objectives:
  - 캡슐화(Encapsulation) 복습 / Encapsulation review
  - Read-only 속성 만들기 / Read-only attributes
  - Setter에서 raise ValueError로 검증 / Validation with raise ValueError

이 파일을 실행하면 에러 없이 돌지만, 테스트는 모두 실패합니다.
This file runs without errors, but all tests will fail.
TODO를 하나씩 채워가며 완성하세요!
Fill in the TODOs one by one!
"""

from datetime import date


class GymMembership:
    """
    헬스장 회원권 클래스 / Gym Membership class
    
    캡슐화 원칙 / Encapsulation rules:
      - 모든 속성은 _ 접두사로 private 표시
      - Read-only: _member_id, _check_in_count (setter 만들지 않기)
      - 검증 필요: _name, _tier, _expiration_date
      
      - All attributes start with _ (private convention)
      - Read-only: _member_id, _check_in_count (no setter!)
      - Validated: _name, _tier, _expiration_date
    """
    
    # 유효한 등급 목록 (변경하지 마세요) / Valid tiers (don't change)
    VALID_TIERS = ("basic", "premium", "vip")
    
    # ========================================
    # TODO 1: __init__ 메서드 / __init__ method
    # ========================================
    # 파라미터 / Parameters: member_id, name, tier, expiration_date
    # 
    # 해야 할 일 / What to do:
    #   1) member_id 검증: 빈 문자열이면 raise ValueError
    #      Validate member_id: empty string → raise ValueError
    #   2) self._member_id에 저장 / Store in self._member_id
    #   3) self.set_name(name) 호출 (검증 재사용)
    #      Call self.set_name(name) (reuse validation)
    #   4) self.set_tier(tier) 호출 / Call self.set_tier(tier)
    #   5) self.set_expiration_date(expiration_date) 호출
    #   6) self._check_in_count = 0
    #
    # 힌트 / Hint: setter 메서드를 먼저 만든 후 __init__에서 호출하면 검증 로직을 재사용할 수 있어요!
    # Define setters first, then call them from __init__ to reuse validation logic.
    def __init__(self, member_id, name, tier, expiration_date):
        # 여기에 코드 작성 / Your code here
        pass
    
    # ========================================
    # TODO 2: Getter 메서드 5개 / 5 getter methods
    # ========================================
    # 각 속성에 대한 getter를 만드세요 / Make a getter for each attribute
    
    # TODO 2-1: get_member_id() → self._member_id 반환 / return self._member_id
    
    # TODO 2-2: get_name() → self._name 반환 / return self._name
    
    # TODO 2-3: get_tier() → self._tier 반환 / return self._tier
    
    # TODO 2-4: get_expiration_date() → self._expiration_date 반환
    
    # TODO 2-5: get_check_in_count() → self._check_in_count 반환
    
    
    # ========================================
    # TODO 3: Setter 메서드 3개 (검증 포함!) / 3 setters with validation
    # ========================================
    
    # TODO 3-1: set_name(name)
    # 조건 / Conditions:
    #   - name이 문자열이 아니거나 .strip() 결과가 빈 문자열 → raise ValueError
    #     Not a string OR strip() is empty → raise ValueError
    #   - 통과하면 self._name = name.strip()
    #     Otherwise self._name = name.strip()
    
    # TODO 3-2: set_tier(tier)
    # 조건 / Conditions:
    #   - tier가 self.VALID_TIERS에 없으면 → raise ValueError
    #     Not in VALID_TIERS → raise ValueError
    #   - 통과하면 self._tier = tier
    
    # TODO 3-3: set_expiration_date(expiration_date)
    # 조건 / Conditions:
    #   - 문자열이 아니면 → raise ValueError
    #   - "YYYY-MM-DD" 형식으로 파싱 안 되면 → raise ValueError
    #     Hint: try: date.fromisoformat(expiration_date) ... except ValueError: raise ...
    #   - 통과하면 self._expiration_date = expiration_date
    
    
    # ⚠️ 주의 / Warning:
    # set_member_id, set_check_in_count 메서드는 만들지 마세요!
    # DO NOT create set_member_id or set_check_in_count methods!
    # 이 두 속성은 read-only입니다 / These are read-only.
    
    
    # ========================================
    # TODO 4: check_in(today) 메서드
    # ========================================
    # 파라미터 / Parameters: today (str, "YYYY-MM-DD" 형식)
    # 
    # 해야 할 일 / What to do:
    #   1) today를 date 객체로 변환: today_date = date.fromisoformat(today)
    #   2) 만료일을 date 객체로 변환: exp_date = date.fromisoformat(self._expiration_date)
    #   3) today_date > exp_date이면 → raise ValueError("Cannot check in: membership expired ...")
    #   4) 통과하면 self._check_in_count += 1
    def check_in(self, today):
        # 여기에 코드 작성 / Your code here
        pass
    
    
    # ========================================
    # TODO 5: upgrade_tier(new_tier) 메서드
    # ========================================
    # 등급은 올리는 것만 가능 / Tier can only go UP
    # 
    # 해야 할 일 / What to do:
    #   1) new_tier가 self.VALID_TIERS에 없으면 → raise ValueError
    #   2) 현재 순위와 새 순위 계산:
    #      current_rank = self.VALID_TIERS.index(self._tier)
    #      new_rank = self.VALID_TIERS.index(new_tier)
    #   3) new_rank <= current_rank이면 → raise ValueError ("Cannot upgrade ...")
    #   4) 통과하면 self._tier = new_tier
    def upgrade_tier(self, new_tier):
        # 여기에 코드 작성 / Your code here
        pass
    
    
    # ========================================
    # TODO 6: renew(new_expiration_date) 메서드
    # ========================================
    # 만료일 연장 (앞으로만!) / Extend expiration (forward only!)
    #
    # 해야 할 일 / What to do:
    #   1) set_expiration_date의 검증 로직 재사용 (직접 호출 OR 검증 코드 복사)
    #   2) 새 날짜를 date 객체로 변환
    #   3) 현재 만료일도 date 객체로 변환
    #   4) 새 날짜 <= 현재 만료일이면 → raise ValueError
    #   5) 통과하면 self._expiration_date 업데이트
    #
    # 힌트 / Hint: 검증 먼저, 그 다음 비교, 그 다음 저장
    # Validate first → compare → store
    def renew(self, new_expiration_date):
        # 여기에 코드 작성 / Your code here
        pass
    
    
    # ========================================
    # TODO 7: is_active(today) 메서드
    # ========================================
    # 회원권이 아직 유효한지 확인 / Check if membership is still valid
    # 
    # 해야 할 일 / What to do:
    #   - today가 만료일 이전이거나 같으면 True
    #   - 만료일을 넘었으면 False
    #   - Return True if today <= expiration, else False
    def is_active(self, today):
        # 여기에 코드 작성 / Your code here
        pass
    
    
    # ========================================
    # TODO 8: __str__ 메서드
    # ========================================
    # 형식 / Format:
    # GymMembership(id=M007, name=Eunwoo Bae, tier=vip, expires=2027-08-15, check_ins=2)
    def __str__(self):
        # 여기에 코드 작성 / Your code here
        pass


# ============================================================
# 🎪 테스트 / Tests (수정하지 마세요 / Do not modify)
# ============================================================

def run_tests():
    print("=" * 60)
    print("🏋️ GymMembership 테스트 시작 / Starting tests")
    print("=" * 60)
    
    tests_passed = 0
    tests_total = 0
    
    # ----- TEST 1 -----
    tests_total += 1
    try:
        m = GymMembership("M001", "박지우", "basic", "2026-12-31")
        assert m.get_member_id() == "M001"
        assert m.get_name() == "박지우"
        assert m.get_tier() == "basic"
        assert m.get_expiration_date() == "2026-12-31"
        assert m.get_check_in_count() == 0
        print("✅ Test 1: 생성과 getter / Construction and getters")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 1 FAILED: {e}")
    
    # ----- TEST 2: Read-only -----
    tests_total += 1
    try:
        m = GymMembership("M001", "박지우", "basic", "2026-12-31")
        assert not hasattr(m, "set_member_id"), "set_member_id should not exist!"
        assert not hasattr(m, "set_check_in_count"), "set_check_in_count should not exist!"
        print("✅ Test 2: Read-only 속성 / Read-only attributes")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 2 FAILED: {e}")
    
    # ----- TEST 3: Name validation -----
    tests_total += 1
    try:
        m = GymMembership("M001", "박지우", "basic", "2026-12-31")
        m.set_name("이수호")
        assert m.get_name() == "이수호"
        try:
            m.set_name("")
            raise AssertionError("Empty name should have raised ValueError")
        except ValueError:
            pass
        try:
            m.set_name("   ")
            raise AssertionError("Whitespace name should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 3: 이름 검증 / Name validation")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 3 FAILED: {e}")
    
    # ----- TEST 4: Tier validation -----
    tests_total += 1
    try:
        m = GymMembership("M001", "박지우", "basic", "2026-12-31")
        m.set_tier("premium")
        assert m.get_tier() == "premium"
        try:
            m.set_tier("gold")
            raise AssertionError("Invalid tier should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 4: 등급 검증 / Tier validation")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 4 FAILED: {e}")
    
    # ----- TEST 5: Date validation -----
    tests_total += 1
    try:
        m = GymMembership("M001", "박지우", "basic", "2026-12-31")
        m.set_expiration_date("2027-06-15")
        assert m.get_expiration_date() == "2027-06-15"
        try:
            m.set_expiration_date("not-a-date")
            raise AssertionError("Bad date format should have raised ValueError")
        except ValueError:
            pass
        try:
            m.set_expiration_date("2027-13-99")
            raise AssertionError("Invalid calendar date should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 5: 날짜 검증 / Date validation")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 5 FAILED: {e}")
    
    # ----- TEST 6: check_in -----
    tests_total += 1
    try:
        m = GymMembership("M002", "이수호", "basic", "2027-06-30")
        m.check_in("2026-05-18")
        m.check_in("2026-05-19")
        m.check_in("2026-05-20")
        assert m.get_check_in_count() == 3, f"Expected 3, got {m.get_check_in_count()}"
        print("✅ Test 6: check_in 카운터 / check_in counter")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 6 FAILED: {e}")
    
    # ----- TEST 7: Expired check_in -----
    tests_total += 1
    try:
        m = GymMembership("M003", "최하나", "vip", "2026-01-01")
        try:
            m.check_in("2026-05-18")
            raise AssertionError("Expired check-in should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 7: 만료된 check_in 거부 / Expired check-in rejected")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 7 FAILED: {e}")
    
    # ----- TEST 8: upgrade_tier -----
    tests_total += 1
    try:
        m = GymMembership("M004", "한도윤", "basic", "2027-12-31")
        m.upgrade_tier("premium")
        assert m.get_tier() == "premium"
        m.upgrade_tier("vip")
        assert m.get_tier() == "vip"
        try:
            m.upgrade_tier("basic")
            raise AssertionError("Downgrade should have raised ValueError")
        except ValueError:
            pass
        try:
            m.upgrade_tier("vip")
            raise AssertionError("Same-tier upgrade should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 8: 등급 업그레이드 / Tier upgrade")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 8 FAILED: {e}")
    
    # ----- TEST 9: renew -----
    tests_total += 1
    try:
        m = GymMembership("M005", "윤소라", "premium", "2026-12-31")
        m.renew("2027-12-31")
        assert m.get_expiration_date() == "2027-12-31"
        try:
            m.renew("2026-06-01")
            raise AssertionError("Backward renew should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 9: 만료일 연장 / Membership renewal")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 9 FAILED: {e}")
    
    # ----- TEST 10: is_active -----
    tests_total += 1
    try:
        m = GymMembership("M006", "장유나", "basic", "2026-12-31")
        assert m.is_active("2026-05-18") is True
        assert m.is_active("2027-01-01") is False
        print("✅ Test 10: is_active")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 10 FAILED: {e}")
    
    # ----- TEST 11: __str__ -----
    tests_total += 1
    try:
        m = GymMembership("M007", "배은우", "vip", "2027-08-15")
        m.check_in("2026-05-18")
        m.check_in("2026-05-19")
        s = str(m)
        assert "M007" in s and "vip" in s and "2027-08-15" in s
        print(f"✅ Test 11: __str__ → {s}")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 11 FAILED: {e}")
    
    # ----- TEST 12: member_id validation at init -----
    tests_total += 1
    try:
        try:
            GymMembership("", "Test", "basic", "2027-01-01")
            raise AssertionError("Empty member_id should have raised ValueError")
        except ValueError:
            pass
        print("✅ Test 12: member_id 빈 문자열 거부 / Empty member_id rejected")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Test 12 FAILED: {e}")
    
    print("=" * 60)
    print(f"결과 / Result: {tests_passed}/{tests_total} 통과 / passed")
    print("=" * 60)


if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"\n⚠️ 테스트 실행 중 에러 / Error during testing: {e}")
        print("아직 TODO를 다 완성하지 않았다면 정상입니다!")
        print("This is normal if you haven't finished the TODOs yet!")
